#IMPORT LIBRARIES

import tensorflow as tf
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from tensorflow.python import keras
import math
import pickle
import pandas as pd
import numpy as np
import sys

#LOAD THE MODEL

with open('fashion_mnist.pkl','rb') as f:
    model = pickle.load(f)

#DATA PRE-PROCESSING

def data_preprocessing(raw):
    label = tf.keras.utils.to_categorical(raw.label, 10)
    num_images = raw.shape[0]
    x_as_array = raw.values[:,1:]
    x_shaped_array = x_as_array.reshape(num_images, 28, 28, 1)
    image = x_shaped_array / 255
    return image, label

#LOAD THE TEST DATA 

df_test  = pd.read_csv(str(sys.argv[1]))
X_test, y_test = data_preprocessing(df_test)

#EVALUATE THE MODEL

score = model.evaluate(X_test, y_test, steps=math.ceil(10000/32))

#LOSS & ACCURACY

loss = score[0]
accuracy = score[1]

#CONVERTING LOSS & ACCURACY TO STRING FORMAT

s_loss=str(loss)

s_accu=str(accuracy)

#OUTPUT TEXT DOCUMENT

def myprint(s):
    with open('output.txt','a') as f:
        print(s, file=f)
model.summary(print_fn=myprint)

y_pred = model.predict(X_test)
y_pred_classes = np.argmax(y_pred, axis = 1)
y_true = np.argmax(y_test, axis = 1)

confusion_mtx = confusion_matrix(y_true, y_pred_classes) 
cm = str(confusion_mtx)

#LABELS

class_names = ['T-shirt/top',
            'Trouser',
            'Pullover',
            'Dress',
            'Coat',
            'Sandal',
            'Shirt',
            'Sneaker',
            'Bag',
            'Ankle boot']

f1 = classification_report(y_true,y_pred_classes, target_names= class_names)

send=['Loss: '+s_loss+"\n",'Accuracy: '+s_accu+"\n\n", 'Confusion Matrix: \n'+cm+"\n\n",  'Performance Report(Precision, Recall, F1 Score): \n\n'+f1+"\n\n", "This is the dummy paragraph" ]

with open("output.txt","a") as file1:
    file1.writelines(send)
    file1.close()