import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

train_ds = tf.keras.utils.image_dataset_from_directory(
    "DataReduced",
    labels="inferred",
    label_mode="categorical",
    image_size=(128, 128),
    batch_size=32,
    validation_split=0.2,
    subset="training",
    seed=42
)

val_ds = tf.keras.utils.image_dataset_from_directory(
    "DataReduced",
    labels="inferred",
    label_mode="categorical",
    image_size=(128, 128),
    batch_size=32,
    validation_split=0.2,
    subset="validation",
    seed=42
)

normalization_layer = layers.Rescaling(1./255)

train_ds = train_ds.map(lambda x, y: (normalization_layer(x), y))
val_ds   = val_ds.map(lambda x, y: (normalization_layer(x), y))

# Data augmentation pipeline
data_augmentation = keras.Sequential([
    layers.RandomFlip("horizontal"),       
    layers.RandomRotation(0.1),            
    layers.RandomZoom(0.1),                
    layers.RandomContrast(0.1),            
])

augmented_train_ds = train_ds.map(
    lambda x, y: (data_augmentation(x, training=True), y)
)

#Prefetch
AUTOTUNE = tf.data.AUTOTUNE
augmented_train_ds = augmented_train_ds.prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.prefetch(buffer_size=AUTOTUNE)
