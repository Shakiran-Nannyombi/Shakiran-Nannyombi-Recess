import os
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models # type: ignore
from tensorflow.keras.preprocessing.image import ImageDataGenerator # type: ignore
from tensorflow.keras.models import Sequential # type: ignore
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout # type: ignore
from tensorflow.keras.optimizers import Adam # type: ignore

# set random seeds for reproducibility
tf.random.set_seed(42)
np.random.seed(42)

# Define the constant value
IMAGE_SIZE = (256, 256)  # Image size for resizing
BATCH_SIZE = 32  # Batch size for training
EPOCHS = 20  # Number of epochs for training
NUMBER_OF_CLASSES = 2  # Number of classes in the dataset for Crops((diseases, healthy)
ANIMAL_CLASSES = 3  # Number of classes in the dataset for Animals((cat,dog,human)

#Define the dataset directories and the model save path
DATASET_DIR = 'Machine_learning/dataset'
MODEL_SAVE_PATH = 'first_model.h5'