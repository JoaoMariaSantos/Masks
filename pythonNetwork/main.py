import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import tensorflow as tf
import keras
from keras import layers
from keras.layers import Input, Conv2D, MaxPooling2D, Flatten, Dense, concatenate
#import tensorflow_hub as hub

#tensorflow NN from https://www.youtube.com/watch?v=VtRLrQ3Ev-U


# Define the input layers
image_input = Input(shape=(64, 64, 3), name='face')
vector1_input = Input(shape=(2,), name='eye1')
vector2_input = Input(shape=(2,), name='eye2')
vector3_input = Input(shape=(2,), name='mouth')

# Image processing block
x = Conv2D(32, (3, 3), activation='relu')(image_input)
x = MaxPooling2D((2, 2))(x)
x = Flatten()(x)

# Concatenate image features with vector inputs
concatenated_inputs = concatenate([x, vector1_input, vector2_input, vector3_input])

# Dense layers for further processing
x = Dense(128, activation='relu')(concatenated_inputs)
x = Dense(64, activation='relu')(x)

# Output layer with 5 vectors
output = Dense(5, name='output')(x)

# Create the model
model = tf.keras.Model(inputs=[image_input, vector1_input, vector2_input, vector3_input], outputs=output)

# Compile the model with an appropriate optimizer, loss function, and metrics
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])

# Display the model summary
model.summary()