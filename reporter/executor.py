import pandas as pd

from reporter.config import get_databases, get_queries
from reporter.engine import get_engine, execute_query


def run_query(config, query_name):
    queries = get_queries(config)
    databases = get_databases(config)

    if query_name not in queries:
        print(f"Error: query '{query_name}' no encontrada")
        return None

    query = queries[query_name]
    db_name = query["database"]

    if db_name not in databases:
        print(f"Error: database '{db_name}' no encontrada")
        return None

    engine = get_engine(databases[db_name])
    sql = query["sql"]
    params = query.get("params", {})

    print(f"Ejecutando query '{query_name}'...")
    columns, rows = execute_query(engine, sql, params)

    df = pd.DataFrame(rows, columns=columns)
    sheet_name = query.get("sheet_name", query_name)[:31]
    return sheet_name, df


def run_all_queries(config):
    queries = get_queries(config)
    results = {}
    for name in queries:
        result = run_query(config, name)
        if result:
            results[result[0]] = result[1]
    return results
