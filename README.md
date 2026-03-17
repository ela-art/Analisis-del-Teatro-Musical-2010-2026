
## Mapa de inicio de producciones
![Mapa inicios](docs/mapa_inicios_producciones.png)

## Presentación completa del proyecto
[Ver grabación en vídeo] (https://youtu.be/rIwlUlNgwKk)


# Análisis del Teatro Musical en España (2010–2026)

**Autora:** Ela Ruiz González · Data Analyst  
**Estado:** Proyecto completo (modelo estrella implementado)  

Proyecto end-to-end orientado a negocio que analiza el mercado del teatro musical en España mediante la construcción de un dataset propio y un modelo analítico en Power BI. El objetivo es identificar patrones estructurales en producción, pricing, longevidad, giras y comportamiento de la demanda para apoyar decisiones estratégicas.

---

## Contexto y objetivo

El sector carece de fuentes estructuradas y comparables. Este proyecto aborda ese vacío construyendo una base de datos original para responder preguntas de negocio como:

- ¿Cómo evoluciona la producción tras shocks de demanda?
- ¿Qué factores explican la permanencia en cartel?
- ¿Cómo se estructura el pricing del mercado?
- ¿Qué papel juegan las productoras, los teatros y los géneros?

---

## Datos y metodología

Dataset construido desde cero en Python a partir de fuentes públicas (Ministerio de Cultura, SGAE, webs especializadas) y validado con conocimiento sectorial.

- 71 musicales (2010–2026)
- Variables: producción, duración, giras, pricing, asistencia, geografía
- Uso de proxies documentados (precio web, estimaciones de permanencia)

El proceso incluye:
- ETL reproducible (limpieza, normalización, deduplicación)
- EDA para validación de hipótesis
- Modelado final en Power BI

---

## Modelo de datos

El modelo ha sido refactorizado a un **esquema en estrella**:

- `fact_producciones` → unidad de análisis (obra + año_inicio)
- `dim_obra` → género, duración, origen
- `dim_teatro` → ciudad, plaza
- `dim_anio` → contexto temporal
- Tablas auxiliares: pricing y hábitos

Este diseño mejora la consistencia analítica, la escalabilidad y el rendimiento.

---

## Principales hallazgos

- Mercado cíclico con recuperación clara post-pandemia  
- Alta concentración en pocas productoras y en Madrid  
- Predominio de franquicias (~70%)  
- Longevidad concentrada en pocos títulos  
- Jukebox y familiar con mayor permanencia  
- Pricing segmentado con clara jerarquía por escala y teatro  
- Demanda mayoritariamente femenina y sensible a shocks externos  

---

## Implicaciones estratégicas

- Estrenar en fases expansivas del mercado  
- Usar Madrid como hub de validación  
- Priorizar géneros comerciales para estabilidad  
- Combinar franquicias (seguridad) e IP propia (valor)  
- Alinear pricing con posicionamiento, teatro y escala  
- Diseñar estrategias de explotación diferenciadas (cartel vs gira)  

---

## Limitaciones

- Muestra reducida en pricing 2026  
- Ausencia de datos reales de taquilla  
- Uso de proxies (precio web, estimaciones)  
- Heterogeneidad entre plazas y teatros  

---

## Stack técnico

Python (Pandas, NumPy)  
Jupyter Notebook  
Power BI (modelado estrella, DAX, dashboards)  
Git / GitHub  
ChatGPT (asistencia en desarrollo)

---

## Estructura del repositorio

- `/data_raw/` → fuentes originales  
- `/data_interim/` → datasets intermedios  
- `/data_processed/` → datasets finales  
- `/notebooks_eda/` → análisis exploratorio  
- `/notebooks_etl/` → construcción del modelo  
- `/dashboards/` → Power BI final  
- `/docs/` → documentación y entregables  

---

## Cómo recorrer el proyecto

1. Revisar `/notebooks_eda/` para entender el análisis  
2. Continuar con `/notebooks_etl/` (construcción del dataset)  
3. Explorar `/data_processed/`  
4. Abrir dashboards en `/dashboards/`  

---

## Mejoras futuras

- Integrar datos reales de taquilla  
- Ampliar cobertura del dataset  
- Automatizar pipelines  
- Modelos predictivos de permanencia y pricing  

---

## Autora

Ela Ruiz González  
Data Analyst  
elaruizgonzalez@gmail.com

