import glob
import shutil
import os

src_dir = "./data/Flickr_Hurricante_Sandy_Image_Store/"
dst_dir = "./data/image/sandy_flickr_"

count = 0
n = 1

for jpgfile in glob.iglob(os.path.join(src_dir, "*.jpg")):

    if count % 1000 == 0:
        dst_dir = "./data/image/sandy_flickr_" + str(n) + "/"
        print dst_dir
        os.makedirs(dst_dir)
        n += 1

    shutil.copy(jpgfile, dst_dir)
    count += 1
