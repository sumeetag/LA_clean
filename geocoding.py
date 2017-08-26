
# AIzaSyDRylJ8hb93BlDyNxL3HSydtxe6FCm25vg

# AIzaSyAliPnDNmGk0TA6XGVhfYQbP7CbRBdYiWM

import json
import requests


api_key = ['AIzaSyBQ-92nJQ1Lu_TuOfgnnyByY4jHSsXB6dQ', 'AIzaSyDRylJ8hb93BlDyNxL3HSydtxe6FCm25vg', 'AIzaSyAliPnDNmGk0TA6XGVhfYQbP7CbRBdYiWM', 'AIzaSyBm_HUunT-04RmR4md1QtTDqxyB0XguMAI', 'AIzaSyDp0guFJicrKpx_5KAtUfMJ-sSUD0I-Rr0', 'AIzaSyCj13pxA8q8tepMykp_pmZCBlEvgVs95NE']
count = 1
i = 0

with open("./data/la_geo_output_1.txt", "w") as f2:
    with open("./data/la_geo_remaining.txt", 'r') as f:
        for line in f:


            try:


                data = line.strip().split(";")

                loc_name = str(data[4]) + " " + str(data[27])

                if count % 2460 == 0:
                    i += 1
                response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=' + loc_name + '&key=' + api_key [i])
                json_data = json.loads(response.text)
                #json_data = {u'status': u'OK', u'results': [{u'geometry': {u'location': {u'lat': 34.04899899999999, u'lng': -118.353826}, u'viewport': {u'northeast': {u'lat': 34.05034798029149, u'lng': -118.3524770197085}, u'southwest': {u'lat': 34.04765001970849, u'lng': -118.3551749802915}}, u'location_type': u'ROOFTOP'}, u'formatted_address': u'1349 S Dunsmuir Ave, Los Angeles, CA 90019, USA', u'place_id': u'ChIJeWwY7AS5woAR7sFGUCc1XL0', u'address_components': [{u'long_name': u'1349', u'types': [u'street_number'], u'short_name': u'1349'}, {u'long_name': u'South Dunsmuir Avenue', u'types': [u'route'], u'short_name': u'S Dunsmuir Ave'}, {u'long_name': u'Central LA', u'types': [u'neighborhood', u'political'], u'short_name': u'Central LA'}, {u'long_name': u'Los Angeles', u'types': [u'locality', u'political'], u'short_name': u'Los Angeles'}, {u'long_name': u'Los Angeles County', u'types': [u'administrative_area_level_2', u'political'], u'short_name': u'Los Angeles County'}, {u'long_name': u'California', u'types': [u'administrative_area_level_1', u'political'], u'short_name': u'CA'}, {u'long_name': u'United States', u'types': [u'country', u'political'], u'short_name': u'US'}, {u'long_name': u'90019', u'types': [u'postal_code'], u'short_name': u'90019'}, {u'long_name': u'2641', u'types': [u'postal_code_suffix'], u'short_name': u'2641'}], u'partial_match': True, u'types': [u'street_address']}]}
                results = json_data[u'results'][0][u'geometry'][u'location']

                data.append(str(results[u'lat']))
                data.append(str(results[u'lng']))

                f2.write(";".join(data) + "\n")
                count += 1

                if count % 100 == 0:
                    print count

            except:
                print line