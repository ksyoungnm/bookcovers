# This module converts raw data in the json files to numpy arrays and saves them on the disk

# System access and json utilities
import sys
import json

# Image manipulation utilities
import numpy as np
import cv2
from urllib.request import urlopen

# target raw data
FILENAME = 'rawdata/amazonOut.json'
with open(FILENAME) as f:
    data = json.load(f)

covers, ratings = [],[]
for item in data:
    if 'cover' in item.keys():
        covers.append(item['cover'])
    else:
        ratings.append(float(item['rating'][0:3].replace(',','.')))

###########
# data manipulation following

# change ratings into an ndarray, the normalize between 0 and 1
ratings = np.asarray(ratings)
ratings /= 5
np.save('rawdata/ratings.npy',ratings)

# trim the number of covers, because more covers than ratings.
covers = covers[0:len(ratings)]
# downloading images, then processing to normalize size and add to a list of image arrays
arrays = []
for i,cover in enumerate(covers):
    reqst = urlopen(cover)
    imgarray = np.asarray(bytearray(reqst.read()), dtype='uint8')
    img = cv2.imdecode(imgarray, cv2.IMREAD_COLOR)
    img = cv2.resize(img, dsize=(136,218))
    img = img / 255
    arrays.append(img)
    sys.stdout.write("\rFinished %d out of %d."%((i+1),len(ratings)))
    sys.stdout.flush()

# finally saves arrays to disk
print()
arrays = np.asarray(arrays)
np.save('rawdata/arrays.npy',arrays)











