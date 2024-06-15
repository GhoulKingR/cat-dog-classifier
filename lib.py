import cv2
import os
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout
from tensorflow.keras.applications import EfficientNetB0

def build_model():
    fname = os.path.dirname(__file__)
    weight_path = os.path.join(fname, 'model_weights.weights.h5')
    
    base_model = EfficientNetB0(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
    model = Sequential([
        base_model,
        GlobalAveragePooling2D(),
        Dropout(0.5),
        Dense(1, activation='sigmoid')
    ])
    model.build(input_shape=(None, 224, 224, 3))
    model.load_weights(weight_path)
    return model

def load_and_preprocess_image(image_path, target_size=(224, 224)):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, target_size)
    return image

def cat_or_dog(image_src: str):
    image = load_and_preprocess_image(image_src)
    img_b = np.expand_dims(image, axis=0)
    model = build_model()
    return 'cat' if model.predict(img_b)[0] < 0.5 else 'dog'