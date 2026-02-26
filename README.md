# Clasificación de Frutas - Novateam 🍎🍌🍇

Repositorio del trabajo realizado por el equipo **Novateam**  
Diplomado en Inteligencia Artificial – Nivel Intermedio  
Universidad de Antioquia (UdeA) en convenio con TalentoTech

---

## 🎯 Objetivo del proyecto

Clasificar frutas utilizando **Redes Neuronales Convolucionales (CNN)**, 
evaluando distintos modelos, arquitecturas e hiperparámetros con el fin de:

- Comparar métricas de rendimiento
- Identificar el mejor modelo de clasificación
- Analizar overfitting y generalización
- Documentar resultados de forma reproducible

---

## 👥 Integrantes del equipo

- **Alexandra García** – Ingeniería de Software  
- **Christian** – Ingeniería Electrónica  
- **Sebastián Giraldo** – Ingeniería Biomédica  
- **Andrés Medina** – Ingeniería Electrónica  

Equipo: **Novateam**

---

## 🧠 Flujo de trabajo del equipo (OBLIGATORIO)

- ❌ Nadie trabaja directamente sobre `main`
- ✅ Todo el desarrollo se hace desde `dev`
- ✅ Cada integrante crea su propia rama:
  - `experimento-cnn-nombre`
- ✅ Los cambios se integran mediante **Pull Request**
- ✅ La líder técnica valida e integra a `main`

---

## 📁 Estructura del proyecto

```text
Clasificaciondefrutas.udea.novateam/
│
├── data/
│   ├── raw/            # Dataset original (.zip descomprimido) ❌ NO se sube
│   └── processed/      # Datos procesados ❌ NO se sube
│
├── notebooks/
│   ├── README.md       # Descripción de notebooks
│   └── *.ipynb         # Experimentos y pruebas
│
├── src/
│   ├── __init__.py
│   └── utils.py        # Funciones reutilizables
│
├── models/             # Modelos entrenados ❌ NO se suben
│
├── reports/            # Resultados, métricas, gráficas
│
├── .gitignore
├── requirements.txt
└── README.md
