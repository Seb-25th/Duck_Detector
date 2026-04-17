import tensorflow as tf
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D,MaxPool2D,Flatten
from Augmentation import augmented_train_ds, val_ds
#from tensorflow.keras import layers, models
#from tensorflow.keras.applications import MobileNetV2


model = Sequential()

model.add(Conv2D(filters=32, kernel_size=3, padding='same', activation='relu', input_shape=[128,128,3]))
model.add(Conv2D(filters=32, kernel_size=3, padding='same', activation='relu'))

model.add(Conv2D(filters=64, kernel_size=3, padding='same', activation='relu'))
model.add(Conv2D(filters=64, kernel_size=3, padding='same', activation='relu'))
model.add(MaxPool2D(pool_size=2, strides=1))

model.add(Conv2D(filters=128, kernel_size=3, padding='same', activation='relu'))
model.add(Conv2D(filters=128, kernel_size=3, padding='same', activation='relu'))
model.add(MaxPool2D(pool_size=2, strides=1))

model.add(Flatten())

model.add(Dense(units=128, activation='relu', dtype='float32'))

model.add(Dense(units=5, activation='softmax', dtype='float32'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

model.summary()

trainingHistory = model.fit(augmented_train_ds, validation_data=val_ds, epochs=40)

model.save('a.h5')
