import os
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def load_selected_classes(path, classes, img_size=(100, 100), batch_size=32, validation_split=0.2):
    """
    Carga solo las clases seleccionadas desde la carpeta path.
    
    Args:
        path (str): Carpeta donde están las imágenes organizadas en subcarpetas por clase.
        classes (list): Lista con los nombres de las 10 clases a usar.
        img_size (tuple): Tamaño de las imágenes.
        batch_size (int): Tamaño del batch.
        validation_split (float): Porcentaje de datos para validación.
    
    Returns:
        train_data, val_data: Generadores de Keras para entrenamiento y validación.
    """
    
    datagen = ImageDataGenerator(
        rescale=1./255,
        validation_split=validation_split
    )
    
    train_data = datagen.flow_from_directory(
        path,
        target_size=img_size,
        classes=classes,
        batch_size=batch_size,
        subset='training',
        shuffle=True
    )
    
    val_data = datagen.flow_from_directory(
        path,
        target_size=img_size,
        classes=classes,
        batch_size=batch_size,
        subset='validation',
        shuffle=True
    )
    
    return train_data, val_data