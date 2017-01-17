#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
import MySQLdb as mdb
from sys import argv
#JSON_DIR = r"C:\Users\tom\Downloads\170117-20170117T132541Z\170117"
JSON_DIR = r"C:\Users\tom\Downloads\170117-20170117T132541Z\photos_170117"

allTables = ("Details", "Pics", "User", "Places", "Addr")


insertAddrQuery = """INSERT INTO DbMysql17.Addr (googlePlaceId, city, street, house_number, lat, lon)
VALUES (%s, %s, %s, %s, %s, %s);"""


getAddrIdQuery = """SELECT idAddr 
FROM DbMysql17.Addr
WHERE googlePlaceId = %s"""

insetPhotoQuery = """INSERT INTO DbMysql17.Pics (googleId, url, width, height)
VALUES (%s, %s, %s, %s);"""


insertPlaceQuery = """INSERT INTO DbMysql17.Places (addr_id, name, rating, googleId, type)
VALUES (%s, %s, %s, %s, %s);"""

checkGoogleIdQuery = """SELECT googleId 
FROM DbMysql17.Places
WHERE googleId = %s
AND type = %s"""


"""
input - a row from the jason data file as a dictionary.
output - the addrId from Addr table matching the point in the jason row. if no point is found, returns None.
	If the point is found, but does not yet exist in the DB, it is created, and the AddrId given to it is returned.
"""
def getOrCreateAddrId(jasonData, cur):
	googlePlaceId = jasonData["place_id"]

	cur.execute(getAddrIdQuery, (googlePlaceId,))
	fetched = cur.fetchone()
	if fetched != None:
		if type(fetched) == long:
			return fetched
		return fetched[0]

	lat = None
	lon = None
	if "location" in jasonData:
		loc = jasonData["location"]
		if "lat" in loc and "lng" in loc:
			lat = loc["lat"]
			lon = loc["lng"]
		else:
			print "Bad line - location does not have lat and lng.", loc


	street = None
	house = None
	city = None
	if "formatted_address" in jasonData:
		addr = jasonData["formatted_address"]
		for field in addr.split(","):
			if " St " in field:
				street = field.split(" St ")[0]
				house = field.split(" St ")[1]
				if not house.isdigit():
					house = None
			if "Tel Aviv-Yafo" in field:
				city = "Tel Aviv-Yafo"
	cur.execute(insertAddrQuery, (googlePlaceId, city, street, house, lat, lon))
	cur.execute(getAddrIdQuery, (googlePlaceId,))
	fetched = cur.fetchone()[0]
	if type(fetched) in (type(None), long):
		return fetched
	return fetched[0]
	
def isPlaceIndexed(placeType, googleId, cur):
	cur.execute(checkGoogleIdQuery, (googleId,placeType))
	return cur.fetchone() != None

googleNames = {"Restaurant":["food", "restaurant", "meal_delivery"], 
	"Bar":["bar"], "Club":["night_club"], "Hotel":["lodging"], 
	"Shop":["shoe_store", "book_store", "jewelry_store", "clothing_store"]}
def parsePlace(placeType, jsonData, cur):
	isFound = False
	for name in googleNames[placeType]:
		if name in jsonData["types"]:
			isFound = True
			break
	if isFound:
		addrId = getOrCreateAddrId(jsonData, cur)
		name = jsonData["name"]
		if name.startswith("JAPANIKA"):
			open(r"C:\Users\tom\Desktop\test.txt", "wb").write(name)
		googleId = jsonData["id"]
		if isPlaceIndexed(placeType, googleId, cur):
			return #this place is already in the DB
		rating = None
		if "rating" in jsonData:
			rating = jsonData["rating"]
		cur.execute(insertPlaceQuery, (addrId, name, rating, googleId, placeType))

def parsePhoto(jsonData, cur):
	googleId = jsonData["id"]
	url = jsonData["photo_reference"]
	width = None
	height = None
	if "width" in jsonData:
		width = jsonData["width"]
	if "height" in jsonData:
		height = jsonData["height"]
	cur.execute(insetPhotoQuery, (googleId, url, width, height))


def addFromJsons(conn):
	for root, dirs, files in os.walk(JSON_DIR):
	    for name in files:
	    	FILE_NAME = os.path.join(root, name)
	        print("working on", FILE_NAME)
	        with open(FILE_NAME) as jsonFile:
		        cur = conn.cursor()
	        	#jsonData = json.load(jsonFile)
	        	for line in jsonFile.read().replace("false", "False").replace("true", "True").split("\n"):
	        		if line == "": 
	        			continue
	        		jsonData = eval(line)
	        		#TODO: should we add the hebrew names as well?
	        		if "name" in jsonData and "types" in jsonData and "id" in jsonData and "place_id" in jsonData:
	        			#this is a place record.
		        		for table in ["Restaurant", "Bar", "Club", "Hotel", "Shop"]:
		        			parsePlace(table, jsonData, cur)
		        	elif "photo_reference" in jsonData and "id" in jsonData:
		        		parsePhoto(jsonData, cur)


def resetAllTables(conn):
	cur = conn.cursor()	
	for table in allTables:
		resetQuery = """DELETE FROM """+table+"""
WHERE id"""+table+""" >= 0;"""
		cur.execute(resetQuery)



def connectToDB():
	return mdb.connect("127.0.0.1", "DbMysql17", "DbMysql17", "DbMysql17", port=19821, use_unicode=True, charset="utf8")

def disconnectDB(conn):
	conn.commit()
	conn.close()

if __name__ == "__main__":
	conn = connectToDB()
	if False:
		print "DELETING ALL TABLES!"
		resetAllTables(conn)
	else:
		addFromJsons(conn)
	disconnectDB(conn)




# DELETE FROM Rests
# WHERE Rests.idRest = 0