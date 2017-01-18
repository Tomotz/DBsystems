#!/usr/bin/env python
# -*- coding: utf-8 -*-


from settings import LOCAL_DB_PASS
import MySQLdb as mdb


MAX_RESULTS = 30 #the maximum number of results to return from a query.

#(googlePlaceId,)
getAddrIdQuery = """SELECT idAddr 
FROM DbMysql17.Addr
WHERE googlePlaceId = %s"""

#(googlePlaceId, city, street, house_number, lat, lon)
insertAddrQuery = """INSERT INTO DbMysql17.Addr (googlePlaceId, city, street, house_number, lat, lon)
VALUES (%s, %s, %s, %s, %s, %s);"""

#(user_name,)
getUserQuery = """SELECT addr_id, user_name, first_name, last_name
FROM DbMysql17.User
WHERE user_name=%s"""

#(idAddr,)
getAddrQuery = """SELECT city, street, house_number, lat, lon, googlePlaceId
FROM DbMysql17.Addr
WHERE idAddr=%s"""

#(addr_id, user_name, first_name, last_name)
insertUserQuery = """INSERT INTO DbMysql17.User (addr_id, user_name, first_name, last_name)
VALUES (%s, %s, %s, %s);"""

#(my_lat, my_lat, my_lon, place_type, radius_in_km)
#This query gets all the places around a given location. Sorted by distance from the location.
placesInDistQuery = """SELECT idPlaces, distanceInKM
FROM
(
	SELECT Places.idPlaces, 
	(
	 2 * 6367.45 * 
	    asin(
			sqrt(
				POWER((sin(radians((Addr.lat - %s) / 2))),2) + 
				cos(radians(%s)) * cos(radians(Addr.lat)) * 
				POWER((sin(radians((Addr.lon - %s) / 2))),2)
			)
		)
	) AS distanceInKM
	FROM Places, Addr
	WHERE Places.addr_id = Addr.idAddr
	AND Places.type = %s
	AND Addr.lat IS NOT NULL
	AND Addr.lon IS NOT NULL
) as sub
WHERE distanceInKM <= %s
ORDER BY distanceInKM    
"""

#(review_text,)
searchInReviewsQuery = """SELECT Places.name, Addr.idAddr, Reviews.text, Reviews.rating 
FROM Reviews, Places, Addr
WHERE Places.addr_id = Addr.idAddr
AND Reviews.googlePlaceId = Addr.googlePlaceId
AND match(Reviews.text) Against('%s' IN BOOLEAN MODE)
"""


class DBUtils:
    conn = mdb.connect("127.0.0.1", "root", LOCAL_DB_PASS, "DbMysql17", port=3306, use_unicode=True, charset="utf8")
    

    '''
    Queries the DB about a specific user.
    Returns the full row matching the user if user was found. Otherwise returns None
    '''
    @classmethod
    def getUserByUname(cls, username):
        cursor = cls.conn.cursor()
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
        cursor = cls.conn.cursor()
        userRow = cls.getUserByUname(username)
        if userRow != None:
            #user already exists!
            return userRow

        idAddr = cls.getOrCreateAddrId(address)
        if None == idAddr:
            #failed to add user!
            return None
        try:
            cursor.execute(insertUserQuery, (idAddr, username, firstName, lastName))
        except Exception, e:
            print "There was an unsupported character in the input"
            print str(e)
            return None
        cls.conn.commit()
        return cls.getUserByUname(username)

    """
    Gets the idAddr of the row in the table mathching the input address. If the row does not exist, it is created.
    input - a location object returned from google
    output - the addrId from Addr table matching the given address
    """
    @classmethod
    def getAddrById(cls, idAddr):
        cursor = cls.conn.cursor()
        cursor.execute(getAddrQuery, (idAddr,))
        row = cursor.fetchone()

        return row

    """
    Gets all the places that has given input words in their text.
    """
    @classmethod
    def getReviewByText(cls, review_text):
        cursor = cls.conn.cursor()
        try:
            cursor.execute(searchInReviewsQuery, (review_text,))
        except Exception, e:
            print "There was an unsupported character in the input"
            print str(e)
            return None
        return cursor.fetchmany(MAX_RESULTS)
	    
    """
    Gets all the places around a given location. Sorted by distance from the location.
    my_lat/my_lon - the latitude and longitude of the given location.
    place_type - a filter for the results - return only results of the given place type
    radius_in_km - the maximum distance of the results to return.
    returns a tuple where each item in the tuple is a tuple itself, containing a line of results.
    If no results match the query, an empty tuple would be returned
    """
    @classmethod
    def aroundMe(cls, my_lat, my_lon, place_type, radius_in_km):
        cursor = cls.conn.cursor()
        try:
            cursor.execute(placesInDistQuery, (my_lat, my_lon, place_type, radius_in_km))
        except Exception, e:
            print "There was an unsupported character in the input"
            print str(e)
            return tuple()
        return cursor.fetchmany(MAX_RESULTS)



    """
    Gets the idAddr of the row in the table mathching the input address. If the row does not exist, it is created.
    input - a location object returned from google
    output - the addrId from Addr table matching the given address
    """
    @classmethod
    def getOrCreateAddrId(cls, address):
        cursor = cls.conn.cursor()
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
        if "formatted_address" in address:
            addr = address["formatted_address"]
            for field in addr.split(","):
                if " St " in field:
                    street = field.split(" St ")[0]
                    house = field.split(" St ")[1]
                    if not house.isdigit():
                        house = None
                if "Tel Aviv-Yafo" in field:
                    city = "Tel Aviv-Yafo"
        try:
            cursor.execute(insertAddrQuery, (googlePlaceId, city, street, house, lat, lon))
        except Exception, e:
            print "There was an unsupported character in the input"
            print str(e)
            return None
        cls.conn.commit()
        cursor.execute(getAddrIdQuery, (googlePlaceId,))
        fetched = cursor.fetchone()[0]
        if type(fetched) in (type(None), long):
            return fetched
        return fetched[0]
