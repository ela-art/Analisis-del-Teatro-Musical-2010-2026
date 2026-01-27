
![Mapa inicios geográficos](docs/mapa_inicios_producciones.png)


Análisis del Teatro Musical en España (2010–2026)
Objetivo

Proyecto de análisis de datos sobre la evolución del teatro musical en España (2010–2026) orientado a identificar:

Patrones de producción

Concentración empresarial

Dinámicas territoriales

Explotación en gira

Características artísticas del sector

El enfoque combina análisis cuantitativo, conocimiento sectorial y visualización en Power BI con foco en la toma de decisiones culturales y de negocio.

Metodología y construcción del dataset

Ante la ausencia de bases de datos centralizadas sobre el sector del teatro musical en España, todos los datasets fueron construidos manualmente desde cero en Python.

Fuentes utilizadas:

Anuario de Estadísticas Culturales (Ministerio de Cultura)

Anuario de la SGAE

Webs oficiales del sector

Archivo de webs especializadas (carteleramusicales.es)

Conocimiento profesional propio del ámbito teatral

Los CSV finales fueron:

Diseñados desde cero

Normalizados y estandarizados

Validados manualmente

Enriquecidos con variables artísticas, territoriales y temporales

Todo el proceso ETL, EDA y modelado se documentó mediante notebooks reproducibles.

Dashboards en Power BI

Dashboards interactivos centrados en:

Evolución del teatro musical (2010–2025)

Actividad de productoras

Pricing del teatro musical (2026)

Inicio geográfico de las producciones

Perfil artístico y estructural

Explotación y comportamiento de giras

Exportaciones disponibles en:

/dashboards/

Datasets finales utilizados
Dataset	Contenido	Uso
maestro_musicales_final.csv	Obras, productoras, teatros, género, origen, años, gira	Estructura sectorial
precios_musicales_limpio_definitivo.csv	Precios publicados 2026	Pricing
teatro_musical_habitos_2011_2025_limpio.csv	Asistencia y hábitos	Demanda

Ubicación:

/data_processed/

Limitaciones del análisis y supuestos

Precios proceden de tarifas web oficiales, no ticket medio real ni ingresos de taquilla.

Muestra reducida en pricing 2026 (5 productoras, 10 títulos).

Ausencia de datos internos de venta u ocupación.

Alta heterogeneidad por plaza y teatro.

Dataset maestro compuesto por 71 musicales seleccionados manualmente.

Dataset de hábitos limitado al periodo visible en las visualizaciones.

Uso de proxies y estimaciones documentadas (semanas en cartel, espectadores).

La longevidad en cartel se calcula incorporando tanto obras cerradas como activas —estimadas hasta la fecha de análisis— lo que permite identificar correctamente casos extremos como El Rey León, The Hole o Forever Young.

Proceso analítico
ETL y preparación

Integración de fuentes institucionales y sectoriales

Normalización de nombres y marcas históricas

Eliminación de duplicados

Validación de tipos y estados

Enriquecimiento con género, origen, ciudad y métricas temporales

Exploración y análisis

Auditoría de calidad

Análisis territorial

Estudio de giras y escalabilidad

Concentración empresarial

Duración media y formatos dominantes

Posicionamiento de precios

Tecnologías

Python (Pandas, NumPy)

Jupyter Notebook

Matplotlib, Seaborn

Power BI

ChatGPT

Git & GitHub

Principales insights

Predominio de franquicias (~73%).

Alta concentración empresarial.

Madrid como principal polo inicial.

Más del 50% de títulos entran en gira.

Duración media estabilizada (~138 minutos).

La longevidad extrema se concentra en unos pocos títulos con explotación sostenida (El Rey León lidera el ranking).

Estructura del repositorio
/
├─ data_raw/
├─ data_interim/
├─ data_processed/
├─ docs/
├─ notebooks_eda/
├─ notebooks_etl/
├─ dashboards/
├─ .gitignore
└─ README.md

Cómo reproducir el proyecto

Clonar el repositorio.

Ejecutar notebooks en /notebooks_etl/.

Revisar análisis en /notebooks_eda/.

Conectar Power BI a los CSV de /data_processed/.

Explorar dashboards exportados en /dashboards/ o /docs/.

Documentación adicional

El PDF final del proyecto se encuentra en:

/docs/


Incluye resumen ejecutivo, storytelling sectorial y visualizaciones clave.

Estado del proyecto

✔ ETL documentado
✔ Modelo relacional con tres datasets
✔ Dashboards Power BI
✔ Storytelling sectorial

Posibles ampliaciones futuras

Series temporales predictivas

Modelos de pricing

Análisis de supervivencia en cartel

Segmentación territorial avanzada

Casos de estudio por producción