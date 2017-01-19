#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
import MySQLdb as mdb
from sys import argv
JSON_DIR = r"C:\Users\tom\Downloads\TDBS"
allTables = ("Details", "Pics", "User", "Places",  "OpenHours", "Addr", "Reviews")


insertAddrQuery = """INSERT INTO DbMysql17.Addr (googlePlaceId, city, street, house_number, lat, lon)
VALUES (%s, %s, %s, %s, %s, %s);"""


getAddrIdQuery = """SELECT idAddr 
FROM Addr
WHERE googlePlaceId = %s"""

insetPhotoQuery = """INSERT INTO Pics (googlePlaceId, url, width, height)
VALUES (%s, %s, %s, %s);"""

insertPlaceQuery = """INSERT INTO Places (addr_id, name, rating, googlePlaceId, type)
VALUES (%s, %s, %s, %s, %s);"""

insetReviewQuery = """INSERT INTO Reviews (rating, text, googlePlaceId)
VALUES (%s, %s, %s);"""

getOpenHoursQuery = """SELECT *
FROM OpenHours
WHERE dayOfWeek = %s
AND googlePlaceId = %s
"""

insetOpenHoursQuery = """INSERT INTO OpenHours (dayOfWeek, hourOpen, hourClose, googlePlaceId)
VALUES (%s, %s, %s, %s);"""

insetDetailsQuery = """INSERT INTO Details (phone, website, googlePlaceId)
VALUES (%s, %s, %s);"""

checkGooglePlaceIdQuery = """SELECT googlePlaceId 
FROM Places
WHERE googlePlaceId = %s
AND type = %s"""

#(idAddr,)
getAddrQuery = """SELECT city, street, house_number, lat, lon, googlePlaceId
FROM Addr
WHERE idAddr=%s"""


"""
input - a row from the Json data file as a dictionary.
output - the addrId from Addr table matching the point in the Json row. if no point is found, returns None.
	If the point is found, but does not yet exist in the DB, it is created, and the AddrId given to it is returned.
"""
def getOrCreateAddrId(jsonData, cur):
	googlePlaceId = jsonData["place_id"]

	cur.execute(getAddrIdQuery, (googlePlaceId,))
	fetched = cur.fetchone()
	if fetched != None:
		if type(fetched) == long:
			return fetched
		return fetched[0]

	lat = None
	lon = None
	if "location" in jsonData:
		loc = jsonData["location"]
		if "lat" in loc and "lng" in loc:
			lat = loc["lat"]
			lon = loc["lng"]
		else:
			print "Bad line - location does not have lat and lng.", loc


	street = None
	house = None
	city = None
	if "city" in jsonData:
		city = jsonData["city"]		
	if "street" in jsonData:
		street = jsonData["street"]	
	if "street_num" in jsonData:
		#actually house num?
		house = jsonData["street_num"]	
		if not house.isdigit():
			house = None

	if "formatted_address" in jsonData:
		#try parsing address from formated addr
		addr = jsonData["formatted_address"]
		for field in addr.split(","):
			if " St " in field and len(field.split(" St "))>1:
				if street == None:
					street = field.split(" St ")[0]
				if house == None:
					house = field.split(" St ")[1]
				if not house.isdigit():
					house = None
			if city == None and "Tel Aviv-Yafo" in field:
				city = "Tel Aviv-Yafo"
	cur.execute(insertAddrQuery, (googlePlaceId, city, street, house, lat, lon))
	cur.execute(getAddrIdQuery, (googlePlaceId,))
	fetched = cur.fetchone()[0]
	if type(fetched) in (type(None), long):
		return fetched
	return fetched[0]
	
def isPlaceIndexed(placeType, googlePlaceId, cur):
	cur.execute(checkGooglePlaceIdQuery, (googlePlaceId,placeType))
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
	if not isFound:
		return 0
	addrId = getOrCreateAddrId(jsonData, cur)
	name = jsonData["name"]
	if name.startswith("JAPANIKA"):
		open(r"C:\Users\tom\Desktop\test.txt", "wb").write(name)
	googlePlaceId = jsonData["place_id"]
	if isPlaceIndexed(placeType, googlePlaceId, cur):
		return 0 #this place is already in the DB
	rating = None
	if "rating" in jsonData:
		rating = jsonData["rating"]
	cur.execute(insertPlaceQuery, (addrId, name, rating, googlePlaceId, placeType))
	return 1

def parsePhoto(jsonData, cur):
	googlePlaceId = jsonData["place_id"]
	url = jsonData["photo_reference"]
	width = None
	height = None
	if "width" in jsonData:
		width = jsonData["width"]
	if "height" in jsonData:
		height = jsonData["height"]
	cur.execute(insetPhotoQuery, (googlePlaceId, url, width, height))
	return 1

def parseReview(jsonData, cur):
	numReviews = 0
	googlePlaceId = jsonData["place_id"]
	for review in jsonData["reviews"]:
		if "rating" not in review:
			continue #not indexing a review without a rating
		rating = review["rating"]
		text = None
		if "text" in review:
			text = review["text"].replace("\xF0\x9F\x98\x89", "")
		cur.execute(insetReviewQuery, (rating, text, googlePlaceId))
		numReviews += 1
	return numReviews

def getAddrById(cur, idAddr):
	cur.execute(getAddrQuery, (idAddr,))
	return cur.fetchone()

def parseAddr(jsonData, cur):
	googlePlaceId = jsonData["place_id"]
	idAddr = getOrCreateAddrId(jsonData, cur)
	if None in getAddrById(cur, idAddr):
		#the record is missing data. we should try updating
		city = None
		street = None
		house_number = None
		lat = None
		lon = None
		columns = ""
		data = []
		if "city" in jsonData:
			data.append(jsonData["city"])
			columns += "city=%s,"
		if "street" in jsonData:
			data.append(jsonData["street"])
			columns += "street=%s,"
		if "street_num" in jsonData:
			#actually house num?
			house_num = jsonData["street_num"]
			if house_num.isdigit():
				data.append(house_num)
				columns += "house_number=%s,"
		if "location" in jsonData:
			loc = jsonData["location"]
			if "lat" in loc and "lng" in loc:
				data.append(loc["lat"])
				data.append(loc["lng"])
				columns += "lat=%s,lon=%s,"
		if columns == "":
			return 0
		else:
			columns = columns[:-1] #remove trailing comma

		data.append(idAddr)
		updateAddrQuery = """UPDATE Addr
SET """+columns+"""
WHERE idAddr=%s;"""
		cur.execute(updateAddrQuery, data)
		return 1
	return 0; #probably didn't add a record

def parseOpenHours(jsonData, cur):
	googlePlaceId = jsonData["place_id"]
	day = jsonData["day"]
	cur.execute(getOpenHoursQuery, (day, googlePlaceId))
	if (cur.fetchone()):
		return 0 #record already exists
	open_hour = jsonData["open_hour"]+"00"
	close_hour = jsonData["close_hour"]+"00"
	cur.execute(insetOpenHoursQuery, (day, open_hour, close_hour, googlePlaceId))
	return 1

def parseDetails(jsonData, cur):
	googlePlaceId = jsonData["place_id"]
	phone = None
	if "phone" in jsonData:
		phone = jsonData["phone"]
	website = None
	if "website" in jsonData:
		website = jsonData["website"]
	cur.execute(insetDetailsQuery, (phone, website, googlePlaceId))
	return 1



#returns true iff all the keys given are in the jsonData
def areAllInJson(jsonData, keys):
	return not (False in [i in jsonData for i in keys])

def addFromJsons(conn):
	countReviews = 0
	countPlace = 0
	countPhoto = 0
	countAddr = 0
	countHours = 0
	countDetails = 0
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
					if areAllInJson(jsonData, ["reviews", "place_id"]) and len(jsonData["reviews"])>0:
						#reviews record
						countReviews += parseReview(jsonData, cur)
					if areAllInJson(jsonData, ["name", "types",  "place_id"]):
						#place record.
						for table in ["Restaurant", "Bar", "Club", "Hotel", "Shop"]:
							countPlace += parsePlace(table, jsonData, cur)
					if areAllInJson(jsonData, ["photo_reference", "place_id"]):
						#photo record
						countPhoto += parsePhoto(jsonData, cur)
					if areAllInJson(jsonData, ["place_id", "city"]):
						countAddr += parseAddr(jsonData, cur)
					if areAllInJson(jsonData, ["place_id", "day", "open_hour", "close_hour"]):
						countHours += parseOpenHours(jsonData, cur)
					if areAllInJson(jsonData, ["place_id", "phone"]) or areAllInJson(jsonData, ["place_id", "website"]):
						countDetails += parseDetails(jsonData, cur)

	print "Added", countPlace, "places,", countHours, "hours,", countDetails, "details,", countPhoto, "photos and ", countReviews, "reviews"
	print "Added or Updated", countAddr, "addresses"

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


