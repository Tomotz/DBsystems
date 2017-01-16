import json
import os
import MySQLdb as mdb

JSON_DIR = r"C:\Users\tom\Desktop\TAU\solutions\DBs\project\example_jsons"

def isHebrew(s):
	return any(u"\u0590" <= c <= u"\u05EA" for c in s)


insertAddrQuery = """INSERT INTO DbMysql17.Addr (city, street, house_number, lat, lon)
VALUES (%s, %s, %s, %s, %s);"""

insertRestsQuery = """INSERT INTO DbMysql17.Rests (addresses_id, name)
VALUES (%s, %s);"""

getAddrIdQuery = """SELECT idAddr 
FROM DbMysql17.Addr
WHERE lat = %s
AND lon = %s"""

"""
input - a row from the jason data file as a dictionary.
output - the addrId from Addr table matching the point in the jason row. if no point is found, returns None.
	If the point is found, but does not yet exist in the DB, it is created, and the AddrId given to it is returned.
"""
def getOrCreateAddrId(jasonData, cur):
	if "location" not in jasonData:
		return None
	loc = jasonData["location"]
	
	if "lat" not in loc or "lng" not in loc:
		print "badLine - No lat or lng"
		return None
	lat = loc["lat"]
	lon = loc["lng"]

	cur.execute(getAddrIdQuery, (lat, lon))
	fetched = cur.fetchone()
	if fetched != None:
		if type(fetched) == long:
			return fetched
		return fetched[0]

	if "formatted_address" in jasonData:
		addr = jasonData["formatted_address"]
		street = None
		house = None
		city = None
		if True: # not isHebrew(addr):
			for field in addr.split(","):
				if " St " in field:
					street = field.split(" St ")[0]
					house = field.split(" St ")[1]
					if not house.isdigit():
						house = None
				if "Tel Aviv-Yafo" in field:
					city = "Tel Aviv-Yafo"
	cur.execute(insertAddrQuery, (city, street, house, lat, lon))
	cur.execute(getAddrIdQuery, (lat, lon))
	fetched = cur.fetchone()[0]
	if type(fetched != long):
		print "returning:", fetched, "of type:", type(fetched)
	if type(fetched) in (type(None), long):
		return fetched
	return fetched[0]
	

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
	        		if "name" not in jsonData or "types" not in jsonData:# or isHebrew(jsonData["name"]):
	        			continue
	        		if "restaurant" in jsonData["types"]:
		        		addrId = getOrCreateAddrId(jsonData, cur)
		        		print addrId

		        		name = jsonData["name"]
		        		cur.execute(insertRestsQuery, (addrId, name))
	        			cur.fetchone()




def connectToDB():
	return mdb.connect("127.0.0.1", "DbMysql17", "DbMysql17", "DbMysql17", port=19821)

def disconnectDB(conn):
	conn.commit()
	conn.close()

if __name__ == "__main__":
	conn = connectToDB()
	addFromJsons(conn)
	disconnectDB(conn)




# DELETE FROM Rests
# WHERE Rests.idRest = 0