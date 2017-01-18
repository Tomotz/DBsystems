from utils import DBUtils
import json

class Serializers:
    @classmethod
    def UserSerizlizer(cls, user_row):
        obj = {
            "address"    : cls.AddressSerializer(DBUtils.getAddrById(user_row[0]), stringify=False),
            "username"   : user_row[1],
            "first_name" : user_row[2],
            "last_name"  : user_row[3],
        }

        return json.dumps(obj)

    @classmethod
    def AddressSerializer(cls, addr_row, stringify=True):
        obj = {
            "city"     : addr_row[0],
            "street"   : addr_row[1],
            "number"   : addr_row[2],
            "place_id" : addr_row[5],
            "location" : {
                "lat": addr_row[3],
                "lng": addr_row[4],
            },
        }

        if stringify:
            return json.dumps(obj)
        else:
            return obj

    @classmethod
    def PlaceSerializer(cls, data):
        if type(data) != list:
            data = [data]

        results = []
        for place_row in data:
            obj = {
                "address"    : cls.AddressSerializers(DBUtils.getAddrById(place_row[0]), stringify=False),
                "username"   : place_row[1],
                "first_name" : place_row[2],
                "last_name"  : place_row[3],
            }
            results.append(json.dumps(obj))

        return str(results)
