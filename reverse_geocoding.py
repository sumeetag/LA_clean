
import json
import requests


api_key = ['AIzaSyBQ-92nJQ1Lu_TuOfgnnyByY4jHSsXB6dQ', 'AIzaSyDRylJ8hb93BlDyNxL3HSydtxe6FCm25vg', 'AIzaSyAliPnDNmGk0TA6XGVhfYQbP7CbRBdYiWM', 'AIzaSyBm_HUunT-04RmR4md1QtTDqxyB0XguMAI', 'AIzaSyDp0guFJicrKpx_5KAtUfMJ-sSUD0I-Rr0', 'AIzaSyCj13pxA8q8tepMykp_pmZCBlEvgVs95NE']

flag = 0
count = 0
count_d = 0

with open("./data/crime_data.csv", "r") as f:
    for line in f:
        if flag == 0:
            flag = 1
            continue

        data = line.strip().split(",")
        lat = data[-2][2:]
        lng = data[-1][:-2]
        count += 1

        if data[2].strip().split("/")[-1] == "2017" :#or data[2].strip().split("/")[-1] == "2017":
            count_d += 1


        #print lat, lng
        #print 'https://maps.googleapis.com/maps/api/geocode/json?latlng='+ (lat) + ',' + (lng) + '&key=' + api_key[0]

        # response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?latlng='+ lat+ ',' + lng + '&key=' + api_key[0])
        # json_data = json.loads(response.text)
        # address_components = json_data[u'results'][0][u'address_components']
        # for items in address_components:
        #     if items[u'types'] == [u'postal_code']:
        #         print items[u'long_name'], items[u'short_name']
        # break
print count
print count_d