# https://andrewpwheeler.wordpress.com/2015/12/28/using-python-to-grab-google-street-view-imagery/
# https://maps.googleapis.com/maps/api/streetview?size=600x300&location=46.414382,10.013988&heading=121.78&pitch=-0.76&key=AIzaSyCc3aT99qLHHQMDTej6sg3oGx8_ry1-K_0
# https://developers.google.com/maps/documentation/streetview/intro?authuser=2



import json
import requests
import urllib, os


#response = requests.get('https://maps.googleapis.com/maps/api/streetview?size=600x300&location=46.414382,10.013988&heading=151.78&pitch=-0.76&key=AIzaSyCc3aT99qLHHQMDTej6sg3oGx8_ry1-K_0')
#json_data = json.loads(response.text)

SaveLoc = './data/gsv/'

api_key = ['AIzaSyC7otZHPWobeec1qt1dq9oyp9tX40F8xz0', 'AIzaSyCCs3U09LiyYwi14PLdbOwXuO9LvgPf4LM', 'AIzaSyDrBhEaYpnNvC5_T4WK9JN_Onn_7YcJAlg', 'AIzaSyCc3aT99qLHHQMDTej6sg3oGx8_ry1-K_0']

count = 1
n = 0

error = []

with open("./data/la_geo_output_non_duplicate.txt", 'r') as f:
    for line in f:
        data = line.strip().split(";")
        lat = data[-2]
        lng = data[-1]
        image_name = data[-3].split(" ")[-1][:-4]
        print image_name
        print lat
        print lng

        heading = [0, 90, 180, 270]

        for i in heading:
            fi = str(image_name) + "_" + str(lat) + "_" + str(lng) + "_" + str(i) + ".jpg"
            try:
                if count % 24000 == 0:
                    n += 1

                urllib.urlretrieve(
                    "https://maps.googleapis.com/maps/api/streetview?size=640x640&location=" + str(lat) + "," + str(lng) + "&heading=" + str(i) +"&key=" + api_key[n],
                    os.path.join(SaveLoc, fi))

                count += 1

                if count % 200 == 0:
                    print count

            except:

                error.append(str("https://maps.googleapis.com/maps/api/streetview?size=640x640&location=" + str(lat) + "," + str(lng) + "&heading=" + str(i) +"&key=") + "\t" + fi)
                print fi
        break


with open("./data/gsv_remain.txt", 'w') as f1:
    for i in error:
        f1.write(i + "\n")





# urllib.urlretrieve("https://maps.googleapis.com/maps/api/streetview?size=600x300&location=46.414382,10.013988&key=AIzaSyCc3aT99qLHHQMDTej6sg3oGx8_ry1-K_0", os.path.join(SaveLoc,fi))
#
# print response