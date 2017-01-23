#!/usr/bin/python

import urllib2
import json
import time

#types
bar = 'bars'
food = 'food'
night_club = 'night_club'
take_away = 'meal_takeaway'
restaurant = 'restaurant'
hotel = 'lodging'
store = 'store'
clothing_shop = 'clothing_store'
shoe_store = 'shoe_store'

TYPES = [food, restaurant, take_away, night_club, bar, hotel, store, clothing_shop, shoe_store]

#locations
ramat_hahayal = '32.112728,34.837846'
ramat_aviv = '32.113290,34.795666'
ibn_gabirol = '32.083140,34.781476'
sarona = '32.071826,34.787461'
ben_yehuda = '32.082804,34.771370'
hayarkon = '32.072421,34.765588'
rothschild = '32.071638,34.779310'
levinsky = '32.060323,34.773928'
jaffa = '32.057090,34.760099'
hamedina_square = '32.088540,34.791645'
yad_aliyahu = '32.057886,34.793431'
dizenguff_square = '32.078170,34.774152'
port = '32.095630,34.772712'

LOCATIONS = [hamedina_square, yad_aliyahu, dizenguff_square, ramat_hahayal, ramat_aviv, ibn_gabirol, sarona, ben_yehuda,
             hayarkon, rothschild, levinsky, jaffa]
LOCATIONS_NAMES = ['hamedina_square', 'yad_aliyahu', 'dizenguff', 'ramat_hahayal', 'ramat_aviv', 'ibn_gabirol',
                   'sarona', 'ben_yehuda', 'hayarkon', 'rothschild', 'levinsky', 'jaffa']


URL = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='
RADIUS = '&radius=1500&type='
KEY = '&key=AIzaSyD_nf1ob13G9wRi_cupAAaJ9iun2vcBGgo'
PAGES = 10


for loc in LOCATIONS:
    for search_type in TYPES:
        first_request = URL + loc + RADIUS + search_type + KEY
        request = first_request
        for i in range(PAGES):
            location_name = LOCATIONS_NAMES[LOCATIONS.index(loc)]
            response = urllib2.urlopen(request).read()
            parsed_json = json.loads(response)
            with open('location_search_output/' + location_name + '_' + search_type + '_' + str(i) + '.json', 'w') as outfile:
                json.dump(parsed_json, outfile)
            outfile.close()
            try:
                next_page_token = parsed_json['next_page_token']
                request = first_request + '&pagetoken=' + next_page_token
                time.sleep(3)
            except KeyError:
                print(location_name + '_' + search_type + ' stopped at index: ' + str(i) + '\n')
                break

