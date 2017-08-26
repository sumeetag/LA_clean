# import os
# n = 1
#
# for filename in os.listdir("./data/image/"):
#
#     print filename
#     if filename.startswith("flickr"):
#         print "Asd"
#         os.rename(filename, "Flickr_Hurricane_Sandy_Image_Dataset_Batch" + str(n))
#         n += 1


import glob
import os

n = 1

files = glob.glob('./data/image/flickr*')
for file in files:
    print file
    os.rename(file, "./data/image/Flickr_Hurricane_Sandy_Image_Dataset_Batch" + str(n))
    n += 1