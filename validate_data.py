# validate_data.py
# Validacion automatica de los CSV generados por el pipeline ETL.
# Ejecutar desde la raiz del proyecto: python validate_data.py

import pandas as pd
import sys

errors = []

def check(label, condition, detail=""):
    if condition:
        print(f"  [OK]   {label}")
    else:
        msg = f"  [FAIL] {label}"
        if detail:
            msg += f" -- {detail}"
        print(msg)
        errors.append(label)

def section(title):
    print(f"\n{'-'*55}")
    print(f"  {title}")
    print(f"{'-'*55}")

# CARGA
try:
    fact    = pd.read_csv("data_processed/fact_producciones.csv",                    encoding="utf-8-sig")
    obra    = pd.read_csv("data_processed/dim_obra.csv",                             encoding="utf-8-sig")
    teatro  = pd.read_csv("data_processed/dim_teatro.csv",                           encoding="utf-8-sig")
    anio    = pd.read_csv("data_processed/dim_anio.csv",                             encoding="utf-8-sig")
    precios = pd.read_csv("data_processed/precios_musicales_limpio_definitivo.csv",  encoding="utf-8-sig")
    maestro = pd.read_csv("data_raw/maestro_musicales.csv",                          encoding="utf-8-sig")
except FileNotFoundError as e:
    print(f"\n[FAIL] Archivo no encontrado: {e}")
    print("  Ejecuta primero notebooks_etl/01_ETL_star_schema.ipynb")
    sys.exit(1)

# FACT_PRODUCCIONES
section("fact_producciones")
check("Filas >= 72",                     len(fact) >= 72,              f"encontradas: {len(fact)}")
check("Sin nulos en id_produccion",      fact["id_produccion"].isna().sum() == 0)
check("Sin nulos en obra",               fact["obra"].isna().sum() == 0)
check("Sin nulos en anio_inicio",        fact["anio_inicio"].isna().sum() == 0)
check("Sin nulos en id_obra",            fact["id_obra"].isna().sum() == 0)
check("Sin nulos en id_teatro",          fact["id_teatro"].isna().sum() == 0)
check("Sin duplicados en id_produccion", fact["id_produccion"].duplicated().sum() == 0,
      f"{fact['id_produccion'].duplicated().sum()} duplicados")
fuera = fact[~fact["anio_inicio"].between(2010, 2026)]["anio_inicio"].tolist()
check("anio_inicio en rango 2010-2026",  len(fuera) == 0, f"fuera de rango: {fuera}")

# DIM_OBRA
section("dim_obra")
check("Filas >= 67",              len(obra) >= 67,  f"encontradas: {len(obra)}")
check("Sin nulos en id_obra",     obra["id_obra"].isna().sum() == 0)
check("Sin nulos en obra",        obra["obra"].isna().sum() == 0)
check("Sin nulos en genero",      obra["genero"].isna().sum() == 0)
check("Sin nulos en origen",      obra["origen"].isna().sum() == 0)
check("Sin nulos en duracion",    obra["duracion"].isna().sum() == 0)
check("IDs unicos en id_obra",    obra["id_obra"].duplicated().sum() == 0)
check("Obras unicas",             obra["obra"].duplicated().sum() == 0,
      f"{obra['obra'].duplicated().sum()} duplicadas")
dur_fuera = obra[~obra["duracion"].between(30, 300)]["duracion"].tolist()
check("Duracion en rango 30-300 min", len(dur_fuera) == 0, f"fuera de rango: {dur_fuera}")

# DIM_TEATRO
section("dim_teatro")
check("Filas = 28",               len(teatro) == 28, f"encontradas: {len(teatro)}")
check("Sin nulos en id_teatro",   teatro["id_teatro"].isna().sum() == 0)
check("Sin nulos en teatro",      teatro["teatro"].isna().sum() == 0)
check("Sin nulos en ciudad",      teatro["ciudad"].isna().sum() == 0)
check("IDs unicos en id_teatro",  teatro["id_teatro"].duplicated().sum() == 0)
check("Teatros unicos",           teatro["teatro"].duplicated().sum() == 0)

# DIM_ANIO
section("dim_anio")
check("Filas = 15",               len(anio) == 15,  f"encontradas: {len(anio)}")
check("Sin nulos en id_anio",     anio["id_anio"].isna().sum() == 0)
check("Sin nulos en anio",        anio["anio"].isna().sum() == 0)
check("IDs unicos en id_anio",    anio["id_anio"].duplicated().sum() == 0)
check("Anos unicos",              anio["anio"].duplicated().sum() == 0)
check("Anos ordenados",           list(anio["anio"]) == sorted(anio["anio"].tolist()))

# PRECIOS
section("precios_musicales_limpio_definitivo")
check("Columna id_obra presente",         "id_obra" in precios.columns)
check("precio_min > 0 en todas las filas",
      (precios["precio_min"] > 0).all(),
      f"{(precios['precio_min'] <= 0).sum()} filas con precio_min <= 0")
check("precio_max >= precio_min",
      (precios["precio_max"] >= precios["precio_min"]).all())

# INTEGRIDAD REFERENCIAL
section("Integridad referencial")
ids_obra_dim    = set(obra["id_obra"])
ids_obra_fact   = set(fact["id_obra"].dropna().astype(int))
ids_teatro_dim  = set(teatro["id_teatro"])
ids_teatro_fact = set(fact["id_teatro"].dropna().astype(int))

huerfanos_obra   = ids_obra_fact - ids_obra_dim
huerfanos_teatro = ids_teatro_fact - ids_teatro_dim
check("id_obra de fact existen en dim_obra",   len(huerfanos_obra) == 0,
      f"IDs huerfanos: {huerfanos_obra}")
check("id_teatro de fact existen en dim_teatro", len(huerfanos_teatro) == 0,
      f"IDs huerfanos: {huerfanos_teatro}")

# RESULTADO
print(f"\n{'='*55}")
if errors:
    print(f"  [FAIL] {len(errors)} error(es) encontrado(s):")
    for e in errors:
        print(f"    - {e}")
else:
    print("  [OK]  Todas las validaciones pasaron correctamente.")
print(f"{'='*55}\n")

sys.exit(1 if errors else 0)
