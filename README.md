# python-sql-reporter

CLI en Python que extrae datos de bases SQL y genera reportes Excel formateados. Soporta multiples motores via SQLAlchemy.

## Que hace

- Se conecta a SQL Server, MySQL, PostgreSQL o SQLite
- Ejecuta queries definidas en un archivo YAML
- Genera un Excel con una hoja por query, headers estilizados y auto-ajuste de columnas

## Uso

```bash
# Instalar dependencias
pip install -r requirements.txt

# Copiar config y editar con tus datos
cp reports.yaml.example reports.yaml

# Ejecutar todas las queries, genera report.xlsx
python main.py run

# Ejecutar una query especifica
python main.py run --query ventas_mes

# Output personalizado
python main.py run --output /path/to/reporte.xlsx

# Listar queries configuradas
python main.py list

# Config alternativo
python main.py run --config mi_config.yaml
```

## Configuracion (`reports.yaml`)

```yaml
databases:
  produccion:
    engine: mssql+pyodbc
    host: localhost
    port: 1433
    database: mydb
    user: sa
    password: "tu_password"
    driver: "ODBC Driver 17 for SQL Server"

  mysql_local:
    engine: mysql+pymysql
    host: localhost
    port: 3306
    database: testdb
    user: root
    password: "tu_password"

  sqlite_demo:
    engine: sqlite
    database: demo.db

queries:
  ventas_mes:
    database: produccion
    sql: "SELECT * FROM ventas WHERE fecha >= :fecha_inicio"
    params:
      fecha_inicio: "2026-01-01"
    sheet_name: "Ventas del Mes"

  stock_actual:
    database: produccion
    sql: "SELECT producto, cantidad FROM stock ORDER BY producto"
    sheet_name: "Stock"
```

## Motores soportados

| Motor | Engine string | Driver requerido |
|-------|--------------|-----------------|
| SQL Server | `mssql+pyodbc` | `pyodbc` + ODBC Driver 17 |
| MySQL | `mysql+pymysql` | `pymysql` |
| PostgreSQL | `postgresql+psycopg2` | `psycopg2` |
| SQLite | `sqlite` | Ninguno (built-in) |

## Formato del Excel

- Headers en negrita, fondo azul oscuro, texto blanco
- Auto-ajuste de ancho de columnas (max 50 chars)
- Formato automatico de fechas y numeros
- Primera fila congelada (freeze panes)
- Una hoja por query

## Estructura del proyecto

```
main.py                # Entry point
reporter/
  cli.py               # argparse CLI
  config.py            # YAML loader
  engine.py            # SQLAlchemy connection manager
  executor.py          # Ejecuta queries, devuelve DataFrames
  excel.py             # Genera Excel formateado
reports.yaml.example   # Config de ejemplo
```

## Dependencias

- Python 3
- sqlalchemy
- pyyaml
- openpyxl
- pandas

## Licencia

MIT
