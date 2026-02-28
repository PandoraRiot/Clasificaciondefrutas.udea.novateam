import os
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Configuración global de NOVATEAM
SELECTED_CLASSES = [
    "Apple Golden 1", "Banana", "Orange", "Lemon", "Strawberry",
    "Kiwi", "Peach", "Pear", "Grape White", "Mango"
]

def load_selected_classes(path, classes=SELECTED_CLASSES, img_size=(100, 100), batch_size=32, validation_split=0.2):
    """
    Carga solo las clases seleccionadas y prepara los generadores.
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

def verify_dataset():
    """
    Verifica físicamente si las carpetas existen antes de intentar cargar.
    """
    base_path = "data/raw/fruits-360-100x100-main/Training"
    print("\n--- 🍎 VERIFICACIÓN DE DATOS NOVATEAM 🍌 ---")
    
    if not os.path.exists(base_path):
        print(f"❌ Error crítico: No se encuentra la ruta {base_path}")
        return False

    found_count = 0
    for fruit in SELECTED_CLASSES:
        path = os.path.join(base_path, fruit)
        if os.path.exists(path):
            print(f"✅ {fruit}: {len(os.listdir(path))} imágenes.")
            found_count += 1
        else:
            print(f"❌ {fruit}: NO ENCONTRADA")
            
    return found_count == 10

if __name__ == "__main__":
    # Si el script se corre directamente, verifica y hace una carga de prueba
    if verify_dataset():
        print("\n🚀 Intentando cargar generadores de Keras...")
        train, val = load_selected_classes("data/raw/fruits-360-100x100-main/Training")
        print(f"\n✨ Éxito: {train.num_classes} clases cargadas correctamente.")
    else:
        print("\n⚠️ Corrige las rutas antes de continuar.")