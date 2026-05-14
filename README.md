# Modelo de Riesgo de Crédito Bancario — PD, EAD y LGD

Sistema de scoring crediticio compuesto por tres modelos que estiman las componentes del riesgo de crédito según el marco regulatorio de Basilea: Probabilidad de Default (PD), Exposición en el Momento del Default (EAD) y Pérdida dado el Default (LGD).

## Tecnologías

Python · Pandas · Scikit-learn · LightGBM · Matplotlib · Jupyter Notebook

## Estructura del repositorio

```
├── 01_Documentos/
│   ├── 003_RIESGOS_Transformaciones.yaml     # Configuración de transformaciones
│   ├── Diccionario.xlsx                       # Diccionario de variables
│   ├── FaseDesarrollo_PlantillaTransf...      # Plantilla fase desarrollo
│   ├── FaseProduccion_PlantillaProc...        # Plantilla fase producción
│   └── stop_words_english.txt                 # Stop words para procesado de texto
│
├── 02_Datos/
│   ├── 01_Originales/
│   │   └── prestamos.csv                      # Dataset original
│   ├── 02_Validacion/
│   │   ├── validacion.csv                     # Dataset de validación
│   │   ├── cat_resultado_calidad.pickle
│   │   ├── cat_resultado_eda.pickle
│   │   ├── df_tablon_lgd.pickle
│   │   ├── df_tablon_sad.pickle
│   │   ├── num_resultado_calidad.pickle
│   │   └── num_resultado_eda.pickle
│   └── 03_Trabajo/
│       ├── trabajo.csv
│       └── trabajo_resultado_calidad.pickle
│
├── 03_Notebooks/
│   ├── 02_Desarrollo/
│   │   ├── 01_Set_Up.ipynb
│   │   ├── 02_Calidad_de_Datos.ipynb
│   │   ├── 03_Exploratory_Data_Analysis.ipynb
│   │   ├── 04_Transformacion_de_datos.ipynb
│   │   ├── 05_Modelizacion_Clasificacion_PD.ipynb
│   │   ├── 06_Modelizacion_Regresion_EAD.ipynb
│   │   ├── 07_Modelizacion_Regresion_LGD.ipynb
│   │   └── 08_Preparacion_del_codigo_de_produccion.ipynb
│   └── 03_Sistema/
│       ├── app_prueba.ipynb                   # Entorno de pruebas
│       ├── app_riesgos.ipynb                  # Aplicación principal
│       ├── 09_Codigo_de_reentrenamiento.ipynb
│       ├── 10_Codigo_de_ejecucion.ipynb
│       └── 10_Codigo_de_ejecucion.py          # Script de producción
│
├── 04_Modelos/
│   ├── pipe_ejecucion_sad.pickle
│   ├── pipe_ejecucion_lgd.pickle
│   ├── pipe_ejecucion_pd.pickle
│   ├── pipe_entrenamiento_sad.pickle
│   ├── pipe_entrenamiento_lgd.pickle
│   ├── pipe_entrenamiento_pd.pickle
│   └── Formula_riesgos.PNG                   # Fórmula de pérdida esperada
│
└── README.md
```

## Los tres modelos

### 1. PD — Probabilidad de Default (Clasificación)
Predice si un préstamo entrará en default.

- **Algoritmo:** Regresión Logística con regularización L1 (exigencia normativa de interpretabilidad)
- **Optimización:** GridSearchCV
- **AUC-ROC sobre validación: 0.881**

### 2. EAD — Exposure at Default (Regresión)
Predice qué porcentaje del crédito disponible estará expuesto en el momento del default.

- **Algoritmo:** HistGradientBoostingRegressor
- **MAPE sobre validación: 0.207**
- **Correlación real vs predicho: 0.72**

### 3. LGD — Loss Given Default (Regresión)
Predice qué porcentaje de la exposición no se recuperará tras el default.

- **Algoritmo:** HistGradientBoostingRegressor
- **MAPE sobre validación: 0.364**
- **Correlación real vs predicho: 0.55**

## Pipeline de producción

El sistema tiene dos modos:

- **Reentrenamiento** (`09_Codigo_de_reentrenamiento.ipynb`): aplica las mismas transformaciones y configuración sobre nuevos datos sin repetir el análisis completo.
- **Ejecución** (`10_Codigo_de_ejecucion.ipynb` / `.py`): carga los pipelines serializados y genera predicciones sobre nuevos datos sin reentrenar.

Los seis pipelines en `04_Modelos/` cubren los tres modelos en sus dos modos (entrenamiento y ejecución).

## Nota sobre el modelo PD

En riesgos bancarios, la normativa (Basilea II/III) exige modelos interpretables. Por eso se usa Regresión Logística en lugar de algoritmos de mayor potencia predictiva. La interpretabilidad no es opcional — es un requisito regulatorio.

## Cómo ejecutarlo

```bash
pip install -r requirements.txt

# Fase desarrollo: ejecutar notebooks en orden desde 03_Notebooks/02_Desarrollo/
# Fase producción: ejecutar 03_Notebooks/03_Sistema/10_Codigo_de_ejecucion.ipynb
```

---

Proyecto académico desarrollado durante el Master en Data Science de Evolve.
