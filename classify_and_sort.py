import tensorflow as tf
import numpy as np
import os
import shutil
classes = ['Agroprom', 'Bar', 'Cordon', 'DarkValley', 'Garbage', 'Last', 'NotLoading', 'UnderAgroprom',
        'WildTerritory', 'YprMonolot', 'army', 'chaes', 'default', 'pripyat', 'radar', 'sarcofag', 
        'x10', 'x16', 'x18', 'yantar']
for item in classes:
    os.mkdir("TestDataResults/"+item)
indexes = []
model = tf.keras.models.load_model("Weights/supernet50.h5")
for item in os.listdir("TestingDataset/TestData2"):
    path_to_file = "TestingDataset/TestData2/"+item
    image = tf.io.decode_png(tf.io.read_file(path_to_file), channels=3)
    image = np.reshape(image,[1,224,224,3] )
    pred = model(image)
    pred = pred.numpy()
    l = list(pred[0])
    ind = l.index(max(l))
    indexes.append(ind)
    shutil.copy(path_to_file,"TestDataResults/"+classes[ind]+"/"+item)


import statistics
def rolling_median(means:list, data:list, scope:int=4):
    for i in range(0,len(data)-scope):
        mode = statistics.mode(data[i:i+scope])
        means.append(mode)

modes = []
rolling_median(modes, indexes)
# plot of loadingscreen classes over image frame 
from matplotlib import pyplot
pyplot.plot(range(0,len(modes)),modes)
pyplot.show()