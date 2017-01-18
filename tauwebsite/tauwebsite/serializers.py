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
        # TODO - implement light places serializer and full single place serializer
        data = list(data)

        results = []
        for place_row in data:
            # image_url = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=1000&maxheight=1000&photoreference=%s&key=AIzaSyD_nf1ob13G9wRi_cupAAaJ9iun2vcBGgo" % place_row[6]
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
