# this module will guess the book rating of any file entered in the input line.
# make sure you have the models generated first.

from keras.models import load_model
import numpy as np
import cv2
import sys,os

try:
    model = load_model('model/bookcovers.h5')
except:
    print("Sorry bud, couldn't load the model!")
    sys.exit(0)

# found the model, so go ahead and enter a file
while(True):
    filepath = input("Give me a filename: ")
    if not (os.path.exists(filepath)):
        print("no bueno, try again please")
        continue
    img = cv2.imread(filepath,cv2.IMREAD_COLOR)
    img = cv2.resize(img, dsize=(136,218))
    img = img / 255
    img = img[np.newaxis,...]
    prediction = model.predict(img)[0] * 5
    print('That is a %.2f star book cover.'%prediction)