from utils import DBUtils
import json

class Serializers:
    @classmethod
    def UserSerizlizer(cls, user_row):
        obj = {
            "id"         : user_row[0],
            "address"    : cls.AddressSerializer(DBUtils.getAddrById(user_row[1]), stringify=False),
            "username"   : user_row[2],
            "first_name" : user_row[3],
            "last_name"  : user_row[4],
        }

        return json.dumps(obj)

    @classmethod
    def AddressSerializer(cls, addr_row, stringify=True):
        obj = {
            "id"       : addr_row[0],
            "city"     : addr_row[1],
            "street"   : addr_row[2],
            "number"   : addr_row[3],
            "location" : {
                "lat": addr_row[4],
                "lng": addr_row[5],
            },
            "place_id" : addr_row[6],
        }

        if stringify:
            return json.dumps(obj)
        else:
            return obj

    @classmethod
    def PlaceSerializer(cls, data):
        data = list(data)

        results = []
        for place_row in data:
            #image_url = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=1000&maxheight=1000&photoreference=%s&key=AIzaSyD_nf1ob13G9wRi_cupAAaJ9iun2vcBGgo" % place_row[6]
            image_url = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=1000&maxheight=1000&photoreference=%s&key=AIzaSyBmNli_ISnmyJxWcPYjCPLB2P8Rbm5dUAQ" % place_row[6]
            obj = {
                "id"           : place_row[0],
                "address"      : cls.AddressSerializer(DBUtils.getAddrById(place_row[1]), stringify=False),
                "name"         : place_row[2],
                "rating"       : place_row[3],
                "google_id"    : place_row[4],
                "type"         : place_row[5],
                "image_url"    : image_url,
                "dist_from_me" : place_row[7],
            }

            results.append(obj)

        return json.dumps(results)

    @classmethod
    def FullPlaceSerializer(cls, place_row):
        pics = []
        for img in place_row[2]:
            #image_url = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=1000&maxheight=1000&photoreference=%s&key=AIzaSyD_nf1ob13G9wRi_cupAAaJ9iun2vcBGgo" % img[2]
            image_url = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=1000&maxheight=1000&photoreference=%s&key=AIzaSyBmNli_ISnmyJxWcPYjCPLB2P8Rbm5dUAQ" % img[2]
            pics.append(image_url)

        reviews = []
        for review_row in place_row[3]:
            review_obj = {
                "id"     : review_row[0],
                "rating" : review_row[1],
                "review" : review_row[2],
            }
            reviews.append(review_obj)

        hours = []
        for hour_row in place_row[4]:
            hour_obj = {
                "id"    : hour_row[0],
                "day"   : hour_row[1],
                "open"  : str(hour_row[2]),
                "close" : str(hour_row[3])
            }
            hours.append(hour_obj)

        obj = {
            "is_open"      : place_row[0],
            "google_id"    : place_row[1][0],
            "name"         : place_row[1][1],
            "address"      : {
                "city"     : place_row[1][2],
                "street"   : place_row[1][3],
                "number"   : place_row[1][4],
                "location" : {
                    "lat": place_row[1][5],
                    "lng": place_row[1][6],
                },
            },
            "phone"        : place_row[1][7],
            "website"      : place_row[1][8],
            "hour_open"    : str(place_row[1][9]),
            "hour_closed"  : str(place_row[1][10]),
            "rating"       : place_row[1][11],
            "rev_rating"   : float(place_row[1][12]) if place_row[1][12] is not None else None,
            "photos"       : pics,
            "reviews"      : reviews,
            "open_hours"   : hours,
        }

        return json.dumps(obj)
