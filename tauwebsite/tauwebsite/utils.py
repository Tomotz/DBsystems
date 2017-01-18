#!/usr/bin/env python
# -*- coding: utf-8 -*-


from settings import LOCAL_DB_PASS
import MySQLdb as mdb


MAX_RESULTS = 1000 #the maximum number of results to return from a query.

######Simple Queries - including insert and update queries############

#input - (idAddr,)
getAddrQuery = """SELECT idAddr, city, street, house_number, lat, lon, googlePlaceId
FROM Addr
WHERE idAddr=%s"""

#input - (googlePlaceId,)
getAddrIdQuery = """SELECT idAddr
FROM Addr
WHERE googlePlaceId = %s"""

#input - (googlePlaceId, city, street, house_number, lat, lon)
insertAddrQuery = """INSERT INTO Addr (googlePlaceId, city, street, house_number, lat, lon)
VALUES (%s, %s, %s, %s, %s, %s);"""

#input - (user_name,)
getUserQuery = """SELECT idUser, addr_id, user_name, first_name, last_name
FROM User
WHERE user_name=%s"""

#input - (addr_id, user_name, first_name, last_name, idUser)
updateUserQuery = """UPDATE User
SET addr_id=%s, user_name=%s, first_name=%s, last_name=%S
WHERE idUser=%s;"""

#input - (addr_id, user_name, first_name, last_name)
insertUserQuery = """INSERT INTO User (addr_id, user_name, first_name, last_name)
VALUES (%s, %s, %s, %s);"""


######Complex Queries - including full text search query############

#this query gets the type of place (Bar/Restaurant/Club/Hotel/Shop) with the highest average rating
bestAvgTypeQuery = """SELECT type
FROM
    (
    SELECT type, avg(rating) as avg_rating
    FROM Places
    GROUP BY type
    ) as sub
WHERE avg_rating =
(
    SELECT MAX(avg_rating)
    FROM
    (
        SELECT avg(rating) as avg_rating
        FROM Places
        GROUP BY type
    ) as sub2
)
"""

#this is a subquery for placesInDist. This query gets one picture url for each place in the Places table.
placeAndPics = """(SELECT idPlaces, addr_id, name, rating, Places.googleId, type, url
FROM Places
JOIN
(
    SELECT googleId, MAX(url) as url
    FROM Pics
    GROUP BY googleId
) as q2
ON Places.googleId = q2.googleId)
"""

#input - (my_lat, my_lat, my_lon, place_type, radius_in_km)
#This query gets all the places around a given location.
placesInDistQuery = """SELECT placePic.idPlaces, addr_id, name, rating, placePic.googleId, type, url, distanceInKM
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
) as sub, """+placeAndPics+""" as placePic
WHERE placePic.idPlaces = sub.idPlaces
AND distanceInKM <= %s
"""

#input - (review_text,)
#FULL TEXT SEARCH QUERY - this query allows the user to search freely for review text
searchInReviewsQuery = """SELECT Places.name, Addr.idAddr, Reviews.text, Reviews.rating 
FROM Reviews, Places, Addr
WHERE Places.addr_id = Addr.idAddr
AND Reviews.googlePlaceId = Addr.googlePlaceId
AND match(Reviews.text) Against('%s' IN BOOLEAN MODE)
"""

#input - (min_num_of_pictures,)
#this query gets all the pictures from places that has more than a given number of pictures
getPictures = """SELECT DISTINCT Places.name, Pics.googlePlaceId, Pics.url, Pics.width, Pics.height
FROM Pics, Places, 
(
    SELECT Pics.googlePlaceId, Count(Pics.googlePlaceId) as num_pictures
    FROM Pics
    GROUP BY Pics.googlePlaceId
    HAVING Count(Pics.googlePlaceId) > %s
) as sub
WHERE Pics.googlePlaceId = Places.googlePlaceId
AND sub.googlePlaceId = Pics.googlePlaceId
ORDER BY sub.num_pictures desc"""



class DBUtils:
    conn = mdb.connect("127.0.0.1", "root", LOCAL_DB_PASS, "DbMysql17", port=3306, use_unicode=True, charset="utf8")


    @classmethod
    def chooseWhatIWantToDo(cls, my_lat, my_lon):
        """This functions gives the user all the results around him from the type of place with the highest rating"""
        placeType = cursor.execute(bestAvgTypeQuery)
        if placeType == None:
            return None
        best = placeType[0]
        return cls.aroundMe(my_lat, my_lon, placeType, 3)


    @classmethod
    def getUserByUname(cls, username):
        '''
        Queries the DB about a specific user.
        Returns the full row matching the user if user was found. Otherwise returns None
        '''
        cursor = cls.conn.cursor()
        cursor.execute(getUserQuery, (username,))
        return cursor.fetchone()

    @classmethod
    def createNewUser(cls, username, firstName, lastName, address):
        '''
        Adds a new user to the DB.
        If the user already exist, the input will be ignored, and the existing user will be returned.
        returns None of failure, otherwise returns the row of the user in the DB.
        address - a google location object matching the user location.
        '''
        cursor = cls.conn.cursor()
        userRow = cls.getUserByUname(username)
        if userRow != None:
            #user already exists!
            return userRow

        idAddr = cls.getOrCreateAddrId(address)
        if None == idAddr:
            #failed to add the address of the user!
            return None
        try:
            cursor.execute(insertUserQuery, (idAddr, username, firstName, lastName))
        except Exception, e:
            print "There was an unsupported character in the input"
            print str(e)
            return None
        cls.conn.commit()
        return cls.getUserByUname(username)

    @classmethod
    def updateUser(cls, username, firstName, lastName, address):
        '''
        Updates an existing user in the DB.
        returns None of failure, otherwise returns the row of the user in the DB.
        address - a google location object matching the user location.
        '''
        cursor = cls.conn.cursor()
        userRow = cls.getUserByUname(username)
        if userRow == None or len(userRow) < 1:
            return None
        idUser = userRow[0]
        idAddr = cls.getOrCreateAddrId(address)
        if None == idAddr:
            #failed to add the address of the user!
            return None
        try:
            cursor.execute(updateUserQuery, (idAddr, username, firstName, lastName, idUser))
        except Exception, e:
            print "There was an unsupported character in the input"
            print str(e)
            return None
        cls.conn.commit()
        return cls.getUserByUname(username)


    @classmethod
    def getAddrById(cls, idAddr):
        """
        Gets the idAddr of the row in the table mathching the input address. If the row does not exist, it is created.
        input - a location object returned from google
        output - the addrId from Addr table matching the given address
        """
        cursor = cls.conn.cursor()
        cursor.execute(getAddrQuery, (idAddr,))
        return cursor.fetchone()

    @classmethod
    def getReviewByText(cls, review_text):
        """
        Gets all the places that has given input words in their text.
        """
        cursor = cls.conn.cursor()
        try:
            cursor.execute(searchInReviewsQuery, (review_text,))
        except Exception, e:
            print "There was an unsupported character in the input"
            print str(e)
            return None
        return cursor.fetchmany(MAX_RESULTS)

    @classmethod
    def aroundMe(cls, my_lat, my_lon, place_type, radius_in_km):
        """
        Gets all the places around a given location. Sorted by distance from the location.
        my_lat/my_lon - the latitude and longitude of the given location.
        place_type - a filter for the results - return only results of the given place type
        radius_in_km - the maximum distance of the results to return.
        returns a tuple where each item in the tuple is a tuple itself, containing a line of results.
        If no results match the query, an empty tuple would be returned
        """
        cursor = cls.conn.cursor()
        placesInDistQuery_orderedByDist = placesInDistQuery + "\nORDER BY distanceInKM"
        try:
            cursor.execute(placesInDistQuery_orderedByDist, (my_lat, my_lat, my_lon, place_type, radius_in_km))
        except Exception, e:
            print "There was an unsupported character in the input"
            print str(e)
            return tuple()
        return cursor.fetchmany(MAX_RESULTS)

    @classmethod
    def topNotch(cls, my_lat, my_lon):
        """
        Gets the best result of each type in radius 3km around the user
        """
        cursor = cls.conn.cursor()
        places = []
        for place_type in ["Restaurant", "Bar", "Club", "Hotel", "Shop"]:
            placesInDistQuery_orderedByDist = placesInDistQuery + "\nORDER BY rating"
            cursor.execute(placesInDistQuery_orderedByDist, (my_lat, my_lat, my_lon, place_type, 3))
            topCatagory = cursor.fetchone()
            if topCatagory != None:
                places.append(topCatagory)
        return places


    @classmethod
    def photographicPlaces(cls, min_num_pics):
        """
        Gets all the photos from restaurants who have min_num_pics or more pictures
        """
        cursor = cls.conn.cursor()
        cursor.execute(getPictures, (min_num_pics, ))
        return cursor.fetchall() #we would like to get more than 30 pictures



    @classmethod
    def getOrCreateAddrId(cls, address):
        """
        Gets the idAddr of the row in the table mathching the input address. If the row does not exist, it is created.
        input - a location object returned from google
        output - the addrId from Addr table matching the given address
        """
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
