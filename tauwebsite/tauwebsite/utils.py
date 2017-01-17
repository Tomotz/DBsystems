#!/usr/bin/env python
# -*- coding: utf-8 -*-


from tauwebsite.tauwebsite.settings import LOCAL_DB_PASS
import MySQLdb as mdb


getAddrIdQuery = """SELECT idAddr 
FROM DbMysql17.Addr
WHERE googlePlaceId = %s"""

insertAddrQuery = """INSERT INTO DbMysql17.Addr (googlePlaceId, city, street, house_number, lat, lon)
VALUES (%s, %s, %s, %s, %s, %s);"""

getUserQuery = """SELECT addr_id, user_name, first_name, last_name
FROM Users 
WHERE user_name=%s"""

insertUserQuery = """INSERT INTO DbMysql17.User (addr_id, user_name, first_name, last_name)
VALUES (%s, %s, %s, %s);"""

class DBUtils:
    conn = mdb.connect("127.0.0.1", "root", LOCAL_DB_PASS, "DbMysql17", port=3306, use_unicode=True, charset="utf8")
    cursor = conn.cursor()

    @classmethod
    '''
    Queries the DB about a specific user.
    Returns the full row matching the user if user was found. Otherwise returns None
    '''
    def getUserByUname(cls, username):
        with cls.cursor as cursor:
            cursor.execute(getUserQuery, (username,))
            row = cursor.fetchone()

        return row


    '''
    Adds a new user to the DB.
    If the user already exist, the input will be ignored, and the existing user will be returned.
    returns None of failure, otherwise returns the row of the user in the DB.
    address - a google location object matching the user location.
    '''
    @classmethod
    def createNewUser(cls, username, firstName, lastName, address):
    	userRow = getUserByUname(cls, username):
    	if userRow != None:
            #user already exists! 
            return userRow

        with cls.cursor as cursor:
        	idAddr = getOrCreateAddrId(cls, address)
        	if None == idAddr:
        		#failed to add user!
        		return None
        	cursor.execute(insertUserQuery, (idAddr, username, firstName, lastName))
			cls.conn.commit()
        return getUserByUname(cls, username)


       




    @classmethod
	"""
	Gets the idAddr of the row in the table mathching the input address. If the row does not exist, it is created.
	input - a location object returned from google
	output - the addrId from Addr table matching the given address
	"""
	def getOrCreateAddrId(cls, address):
        with cls.cursor as cursor:
			googlePlaceId = address["place_id"]

			cursor.execute(getAddrIdQuery, (googlePlaceId,))
			fetched = cursor.fetchone()
			if fetched != None:
				#address was found in the DB. Return it.
				if type(fetched) == long:
					return fetched
				return fetched[0]

			if "lat" in address and "lng" in address:
				lat = address["lat"]
				lon = address["lng"]
			else:
				#user have no lat/lng which is bad.
				return None

			street = None
			house = None
			city = None
			if "formatted_address" in jasonData:
				addr = address["formatted_address"]
				for field in addr.split(","):
					if " St " in field:
						street = field.split(" St ")[0]
						house = field.split(" St ")[1]
						if not house.isdigit():
							house = None
					if "Tel Aviv-Yafo" in field:
						city = "Tel Aviv-Yafo"
			cursor.execute(insertAddrQuery, (googlePlaceId, city, street, house, lat, lon))
			cls.conn.commit()
			cursor.execute(getAddrIdQuery, (googlePlaceId,))
			fetched = cursor.fetchone()[0]
			if type(fetched) in (type(None), long):
				return fetched
			return fetched[0]


# """SELECT idAddr FROM Addr a 
# WHERE 
# (
#   acos(
#   	sin(a.lat * 0.0175) * sin(%s * 0.0175) 
#     + cos(a.lon * 0.0175) * cos(%s * 0.0175) *    
#     cos((%s * 0.0175) - (a.lon * 0.0175))
#   ) * 3959 <= %s
# )
# """, (my_lat, my_lat, my_lon, radius)