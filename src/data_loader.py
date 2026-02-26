# src/data_loader.py

from tensorflow.keras.preprocessing.image import ImageDataGenerator


def get_default_classes():
    """
    Clases base seleccionadas para el proyecto.
    Estas clases deben existir como carpetas dentro del dataset.
    """
    return [
        "Apple Golden 1",
        "Banana",
        "Orange",
        "Lemon",
        "Strawberry",
        "Kiwi",
        "Peach",
        "Pear",
        "Grape White",
        "Mango"
    ]


def load_data(
    data_dir,
    classes,
    batch_size=32,
    img_size=(100, 100),
    shuffle=True
):
    """
    Carga imágenes desde un directorio usando ImageDataGenerator.

    Parámetros:
    - data_dir: ruta a Training o Test
    - classes: lista de clases a cargarcd '/home/kali/proyectos/Clasificaciondefrutas.udea.novateam/Clasificaciondefrutas.udea.novateam'

