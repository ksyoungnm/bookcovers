# Importing the Keras libraries and packages
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D

# loads data into testing and training splits.
images_train,images_test = np.split(np.load('rawdata/arrays.npy'),[4500])
labels_train,labels_test = np.split(np.load('rawdata/ratings.npy'),[4500])

# generating the nerual network. dont ask me how this works
model = Sequential()

model.add(Conv2D(16,(3,3),activation='relu',input_shape=(218,136,3)))
model.add(Conv2D(32,(3,3),activation='relu'))
model.add(Conv2D(64,(3,3),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())
model.add(Dense(16,activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(4,activation='relu'))
# this last neuron needs to be linear to use as a vector regresssion
model.add(Dense(1,activation='linear'))

model.compile(loss='mae',
              optimizer='adam',
              metrics=['mse','mae']
              )

# if you let the model train too long, it just converges to the average of the
# book ratings
model.fit(images_train,labels_train,
          batch_size=45, epochs=2)

# save the weights of the model so we can make predictions
model.save('model/bookcovers.h5')
