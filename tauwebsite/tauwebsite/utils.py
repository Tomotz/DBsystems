#!/usr/bin/env python
# -*- coding: utf-8 -*-


from settings import LOCAL_DB_PASS
import MySQLdb as mdb


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

class DBUtils:
    conn = mdb.connect("127.0.0.1", "root", LOCAL_DB_PASS, "DbMysql17", port=3306, use_unicode=True, charset="utf8")
    cursor = conn.cursor()

    '''
    Queries the DB about a specific user.
    Returns the full row matching the user if user was found. Otherwise returns None
    '''
    @classmethod
    def getUserByUname(cls, username):
        cls.cursor.execute(getUserQuery, (username,))
        row = cls.cursor.fetchone()

        return row

    '''
    Adds a new user to the DB.
    If the user already exist, the input will be ignored, and the existing user will be returned.
    returns None of failure, otherwise returns the row of the user in the DB.
    address - a google location object matching the user location.
    '''
    @classmethod
    def createNewUser(cls, username, firstName, lastName, address):
        userRow = cls.getUserByUname(username)
        if userRow != None:
            #user already exists!
            return userRow

        idAddr = cls.getOrCreateAddrId(address)
        if None == idAddr:
            #failed to add user!
            return None
        cls.cursor.execute(insertUserQuery, (idAddr, username, firstName, lastName))
        cls.conn.commit()
        return cls.getUserByUname(username)

    """
    Gets the idAddr of the row in the table mathching the input address. If the row does not exist, it is created.
    input - a location object returned from google
    output - the addrId from Addr table matching the given address
    """
    @classmethod
    def getAddrById(cls, idAddr):
	    cls.cursor.execute(getAddrQuery, (idAddr,))
	    row = cls.cursor.fetchone()

	    return row

    """
    Gets the idAddr of the row in the table mathching the input address. If the row does not exist, it is created.
    input - a location object returned from google
    output - the addrId from Addr table matching the given address
    """
    @classmethod
    def getOrCreateAddrId(cls, address):
        googlePlaceId = address["place_id"]

        cls.cursor.execute(getAddrIdQuery, (googlePlaceId,))
        fetched = cls.cursor.fetchone()
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
        cls.cursor.execute(insertAddrQuery, (googlePlaceId, city, street, house, lat, lon))
        cls.conn.commit()
        cls.cursor.execute(getAddrIdQuery, (googlePlaceId,))
        fetched = cls.cursor.fetchone()[0]
        if type(fetched) in (type(None), long):
            return fetched
        return fetched[0]
