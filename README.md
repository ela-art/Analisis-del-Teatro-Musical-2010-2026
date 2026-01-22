
🎭 Análisis del Teatro Musical en España (2010–2026)

📌 Objetivo

Este proyecto analiza la evolución del teatro musical en España entre 2010 y 2026 con el objetivo de identificar:

patrones de producción

concentración empresarial

dinámicas territoriales

modelos de explotación (giras)

características artísticas

posicionamiento estructural del sector

El enfoque combina análisis de datos, conocimiento experto del sector escénico y visualización orientada a la toma de decisiones culturales y de negocio.

Proyecto desarrollado como portfolio profesional en Data Analytics, con foco en:

ETL reproducible

análisis exploratorio riguroso

dashboards en Power BI

storytelling sectorial

📊 Dashboards en Power BI

Los análisis finales se presentan mediante dashboards interactivos, entre ellos:

Evolución del teatro musical (2010–2025)

Actividad de productoras

Pricing del teatro musical (2026)

Inicio geográfico de las producciones

Perfil artístico y estructural

Explotación y comportamiento de giras

Las capturas se encuentran en:

/dashboards/

🗂️ Fuentes de datos
Fuentes institucionales

Anuario de Estadísticas Culturales — Ministerio de Cultura

Anuario SGAE de las Artes Escénicas

Fuentes sectoriales y públicas

Carteleras de teatro musical

Webs especializadas

Información pública de productoras y teatros

Curación manual

Normalización y enriquecimiento a partir de conocimiento profesional del sector.

📦 Datasets finales utilizados

El modelo analítico se apoya en tres datasets finales conectados:

Dataset	Contenido	Uso principal
maestro_musicales_final.csv	Obras, productoras, teatros, género, origen, años, gira	Estructura sectorial
precio_entradas_musicales_final.csv	Precios anunciados 2026	Dashboard de pricing
teatro_musical_habitos_2011_2025_limpio.csv	Asistencia y hábitos del público	Demanda agregada

Todos se encuentran en:

/data/processed/

⚙️ Proceso de trabajo
🔹 ETL (Extract · Transform · Load)

Extracción

Integración de fuentes heterogéneas.

Transformación

Normalización de nombres (obras, teatros, productoras).

Unificación de marcas históricas.

Eliminación de duplicados.

Conversión y validación de tipos.

Homogeneización de estados (activa, gira).

Enriquecimiento:

genero

origen

ciudad_teatro

métricas temporales

pricing

Carga

Generación de datasets analíticos finales listos para BI.

🔹 EDA (Exploratory Data Analysis)

Auditoría de calidad.

Cobertura de variables estratégicas.

Detección de patrones.

Análisis territorial.

Escalabilidad vía giras.

Concentración empresarial.

Duración y formatos dominantes.

🧰 Tecnologías y herramientas

Python

Pandas · NumPy

Jupyter Notebook

Matplotlib · Seaborn

Power BI

Git & GitHub

Data Cleaning

ETL pipelines

Data Modeling

Visual Analytics

Storytelling con datos

📈 Principales insights (estado actual)

Predominio de franquicias (~73%).

Baja presencia de creación propia.

Alta concentración empresarial.

Madrid como polo inicial dominante.

Más del 50% de los títulos salen de gira.

Duración media estabilizada (~138 min).

Solo una minoría permanece activa.

El sector prioriza formatos familiares y comedia.

🗃️ Estructura del repositorio
├── data/
│   ├── raw/
│   ├── interim/
│   └── processed/
│
├── notebooks/
│   ├── eda/
│   └── etl/
│
├── dashboards/
│
├── docs/
│
├── README.md
└── .gitignore

▶️ Cómo reproducir el proyecto

Clona el repositorio.

Ejecuta los notebooks en /notebooks/etl/.

Usa los CSV finales en /data/processed/.

Abre el archivo Power BI (.pbix) si se incluye.

Explora dashboards en /dashboards/.

📌 Alcance y consideraciones

El proyecto se basa en una muestra curada de 71 producciones.

No busca exhaustividad absoluta, sino la identificación de tendencias estructurales y patrones de negocio del teatro musical español.

🚧 Estado del proyecto

✔ ETL documentado
✔ Modelo con tres datasets finales
✔ Dashboards Power BI
✔ Storytelling sectorial
⏳ Posibles ampliaciones futuras (automatización, modelo estrella, pricing avanzado)
