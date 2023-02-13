import tensorflow as tf
import numpy as np
import os
import shutil
classes = ['army', 'bar', 'cardon', 'chaes', 'garbage', 'pripyat', 'radar', 'sarcofag']
for item in classes:
    os.mkdir("RunImages/"+item)
# the collab prints this as classes ['army', 'bar', 'cardon', 'chaes', 'garbage', 'pripyat', 'radar', 'sarcofag']
model = tf.keras.models.load_model("LexaNet/.lexanet35.h5")
for item in os.listdir("RunImages/Photo"):
    path_to_file = "RunImages/Photo/"+item
    image = tf.io.decode_png(tf.io.read_file(path_to_file), channels=3)
    image = np.reshape(image,[1,224,224,3] )
    pred = model(image)
    pred = pred.numpy()
    l = list(pred[0])
    ind = l.index(max(l))
    if max(l) > 0.9:
        shutil.move(path_to_file,"RunImages/"+classes[ind]+"/"+item)
    

