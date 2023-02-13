# -*- coding: utf-8 -*-
"""ClassifierNN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oORdub1gP6jGXVItpPC4-i8gbQSI0hy1

Loading and unpacking of the dataset
"""

"""Checking that Data is accurately presented"""
import tensorflow as tf

tf.config.set_soft_device_placement(True)

data_dir = "./StalkerDataset"
train_ds = tf.keras.utils.image_dataset_from_directory(
  data_dir,
  validation_split=0.1,
  subset="training",
  label_mode="categorical",
  seed=123,
  image_size=(224, 224),
  batch_size=16)
val_ds = tf.keras.utils.image_dataset_from_directory(
  data_dir,
  validation_split=0.1,
  subset="validation",
  label_mode="categorical",
  seed=123,
  image_size=(224, 224),
  batch_size=16)

"""Simplest model Possible taken from tensorflow guide
Compilation and training
"""
model = tf.keras.models.Sequential([
    tf.keras.layers.Rescaling(1./255, input_shape=(224, 224, 3)),
    tf.keras.layers.RandomFlip("horizontal_and_vertical"),
    tf.keras.layers.Conv2D(filters=96, kernel_size=(3,3), strides=(1,1), activation='relu', input_shape=(224,224,3)),
    tf.keras.layers.AvgPool2D(pool_size=(3,3), strides=(2,2)),
    tf.keras.layers.AvgPool2D(pool_size=(3,3), strides=(2,2)),
    tf.keras.layers.Conv2D(filters=384, kernel_size=(3,3), strides=(1,1), activation='relu', padding="same"),
    tf.keras.layers.AvgPool2D(pool_size=(3,3), strides=(2,2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(256, activation='relu'),
    tf.keras.layers.Dropout(0.6),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.6),
    tf.keras.layers.Dense(8, activation='softmax')
])
#model = tf.keras.models.load_model(".lexanet24.h5")

model.compile(optimizer=tf.keras.optimizers.SGD(lr=0.001), \
              loss='categorical_crossentropy', \
              metrics=['accuracy', tf.keras.metrics.TopKCategoricalAccuracy(2)])
for i in range(0,100):
  model.fit(train_ds,
           validation_data=val_ds,
           epochs=1)
  model.save("ModificationsNN/modnet"+str(i)+".h5")