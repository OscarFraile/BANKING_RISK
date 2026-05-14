# Modelo de Riesgo de Crédito Bancario — PD, EAD y LGD

Sistema de scoring crediticio compuesto por tres modelos que estiman las componentes del riesgo de crédito según el marco regulatorio de Basilea: Probabilidad de Default (PD), Exposición en el Momento del Default (EAD) y Pérdida dado el Default (LGD).

## Tecnologías

Python · Pandas · Scikit-learn · LightGBM · Matplotlib · Jupyter Notebook

## Estructura del repositorio

```
├── 01_Set_Up.ipynb                          # Configuración del entorno y carga de datos
├── 02_Calidad_de_Datos.ipynb                # Detección y tratamiento de problemas de calidad
├── 03_EDA.ipynb                             # Análisis exploratorio
├── 04_Transformacion_de_datos.ipynb         # Encoding, escalado y creación de variables
├── 05_Modelizacion_Clasificacion_PD.ipynb   # Modelo de Probabilidad de Default
├── 06_Modelizacion_Regresion_EAD.ipynb      # Modelo de Exposición en el Default
├── 07_Modelizacion_Regresion_LGD.ipynb      # Modelo de Pérdida dado el Default
└── 08_Preparacion_del_codigo_de_produccion.ipynb  # Pipelines para producción
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

Los tres modelos están integrados en pipelines serializados que incluyen preprocesado, transformación y predicción. Se ejecutan sobre nuevos datos sin reentrenamiento.

## Cómo ejecutarlo

```bash
pip install -r requirements.txt

# Ejecutar los notebooks en orden numérico
# Empezar por: 01_Set_Up.ipynb
```

## Nota sobre el modelo PD

En riesgos bancarios, la normativa (Basilea II/III) exige modelos interpretables. Por eso se usa Regresión Logística en lugar de algoritmos de mayor potencia predictiva. La interpretabilidad no es opcional — es un requisito regulatorio.

---

Proyecto académico desarrollado durante el Master en Data Science de Evolve.
