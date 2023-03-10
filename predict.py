import tensorflow as tf
import os
import math
def get_num_of_images(path:str):  
    return len(os.listdir(path=path))

tf.config.set_soft_device_placement(True)
images = tf.keras.utils.image_dataset_from_directory("./IndependentData",image_size=(224, 224),shuffle=False, batch_size=32)
classes = images.class_namess
for i in range(0,8):
    #input("press enter to continue")
    weights = "Weights"+str(i)+".h5"
    model = tf.keras.models.load_model(weights)
    predictions = model.predict(images)
    #predictions =  model.predict(images)
    location_to_predictions = {}
    for location in classes:
        image_num = get_num_of_images("./IndependentData/"+location)
        location_to_predictions[location] = predictions[:image_num]
        predictions = predictions[image_num:]
    total = 0
    correct = 0

    for index, location in enumerate(classes):
        preds = location_to_predictions[location]
        for prediction in preds:
            out = "{:<8s}    {}    {}    {:<8s}".format(location,
                                                        max(prediction),
                                                        prediction[index],
                                                        classes[prediction.argmax()])
            #print(out)
            if math.isclose(max(prediction), prediction[index]):
                correct+=1
            total+=1
    #if correct/total >0.5:
    print(weights+" Accuracy: "+str(correct/total))