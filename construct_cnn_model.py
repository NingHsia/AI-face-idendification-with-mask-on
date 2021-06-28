import keras
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout
from keras.optimizers import Adam
from keras.callbacks import TensorBoard

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import roc_curve, auc
from sklearn.metrics import accuracy_score
from keras.utils import np_utils
import itertools
from pathlib import Path
import cv2
import glob

from mtcnn.mtcnn import MTCNN
per_num = 4
def extract_face(path, required_size=(160, 160)):
    print(path)
    pixels = cv2.imread(path)
    detector = MTCNN()
    results = detector.detect_faces(pixels)
    x1, y1, width, height = results[0]['box']
    x1, y1 = abs(x1), abs(y1)
    x2, y2 = x1 + width, y1 + height
    face = pixels[y1:y2, x1:x2]
    face = cv2.resize(face, required_size)
    return face

# combine
imgs = []
idxs = []
per_num = 10
import os, os.path
cnt = 0
train_num = 5
for type in ['withmask/', 'withoutmask/']:
    for i in range(per_num):
        DIR = f"faces/{type}{i}"
        l = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
        # print(f'i:{i}, l:{l}')
        for j in range(train_num):
            path = f"faces/{type}{i}/{j}.jpg"
            img = cv2.imread(path)
            face_pixels = img.astype('float32')
            mean, std = img.mean(), img.std()
            face_pixels = (face_pixels - mean) / std
            imgs.append(face_pixels)
            idxs.append(cnt)   
        cnt+=1
imgs = np.array(imgs)
idxs = np.array(idxs)
print(imgs.shape)
print(idxs.shape)
print(idxs)
label_num = cnt

im_shape=(160, 160, 3)
cnn_model= Sequential([
    Conv2D(filters=36, kernel_size=7, activation='relu', input_shape= im_shape),
    MaxPooling2D(pool_size=2),
    Conv2D(filters=54, kernel_size=5, activation='relu', input_shape= im_shape),
    MaxPooling2D(pool_size=2),
    Flatten(),
    Dense(2024, activation='relu'),
     Dropout(0.5),
    Dense(1024, activation='relu'),
    Dropout(0.5),
    Dense(512, activation='relu'),
    Dropout(0.5),
    #20 is the number of outputs
    Dense(label_num, activation='softmax')  #20
])

cnn_model.compile(
    loss='sparse_categorical_crossentropy',
    optimizer=Adam(lr=0.0001),
    metrics=['accuracy']
)

history=cnn_model.fit(
    imgs, idxs,
    epochs=50, verbose=2,
)

cnn_model.save("cnn_model_5")