
![Mapa inicios geográficos](docs/mapa_inicios_producciones.png)


Análisis del Teatro Musical en España (2010–2026)
Objetivo

Proyecto de análisis de datos sobre la evolución del teatro musical en España (2010–2026) orientado a identificar:

Patrones de producción

Concentración empresarial

Dinámicas territoriales

Explotación en gira

Características artísticas del sector

Combina análisis cuantitativo, conocimiento sectorial y visualización en Power BI con foco en la toma de decisiones culturales y de negocio.

Metodología y construcción del dataset

Ante la ausencia de bases de datos centralizadas sobre el sector del teatro musical en España, todos los datasets del proyecto fueron construidos manualmente desde cero en Python.

La recopilación se realizó a partir de:

Anuario de Estadísticas Culturales (Ministerio de Cultura)

Informes de la SGAE

Webs oficiales del sector y archivo de webs especializadas (carteleramusicales.es)

Conocimiento profesional propio del ámbito teatral

Los archivos CSV finales fueron:

Diseñados desde cero

Normalizados y estandarizados

Validados manualmente

Enriquecidos con variables artísticas, territoriales y temporales

Todo el proceso ETL, EDA y modelado se ejecutó manualmente mediante notebooks reproducibles.

Dashboards en Power BI

El proyecto incluye dashboards interactivos centrados en:

Evolución del teatro musical (2010–2025)

Actividad de productoras

Pricing del teatro musical (2026)

Inicio geográfico de las producciones

Perfil artístico y estructural

Explotación y comportamiento de giras

Capturas y exportaciones disponibles en:

/dashboards/

Datasets finales utilizados

El modelo analítico se apoya en tres tablas principales:

Dataset	Contenido	Uso
maestro_musicales_final.csv	Obras, productoras, teatros, género, origen, años, gira	Estructura sectorial
precios_musicales_limpio_definitivo.csv	Precios anunciados en 2026	Pricing
teatro_musical_habitos_2011_2025_limpio.csv	Asistencia y hábitos	Demanda

Ubicación:

/data_processed/

Limitaciones del análisis

Los precios corresponden a tarifas publicadas en webs oficiales, no a ticket medio real ni ingresos de taquilla.

La muestra de pricing 2026 es reducida (5 productoras y 10 musicales).

No se dispone de datos internos de venta o ocupación.

Existe fuerte heterogeneidad por plaza y teatro.

El dataset maestro contiene 71 musicales seleccionados manualmente.

El dataset de hábitos está limitado al periodo visible en las gráficas.

Algunas métricas utilizan proxies y estimaciones documentadas.

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

Git & GitHub

Principales insights

Predominio de franquicias (~73%).

Alta concentración empresarial.

Madrid como principal polo inicial.

Más del 50% de títulos en gira.

Duración media estabilizada (~138 minutos).

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