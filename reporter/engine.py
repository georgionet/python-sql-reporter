from sqlalchemy import create_engine, text


def build_connection_string(db_config):
    engine_name = db_config["engine"]
    host = db_config.get("host", "localhost")
    port = db_config.get("port", "")
    database = db_config.get("database", "")
    user = db_config.get("user", "")
    password = db_config.get("password", "")

    if engine_name.startswith("sqlite"):
        return f"sqlite:///{database}"

    if engine_name.startswith("mssql"):
        driver = db_config.get("driver", "ODBC Driver 17 for SQL Server")
        port_str = f",{port}" if port else ""
        trust = "yes" if "18" in driver else "no"
        return (
            f"mssql+pyodbc://{user}:{password}@{host}{port_str}/{database}"
            f"?driver={driver}&TrustServerCertificate={trust}"
        )

    port_str = f":{port}" if port else ""
    return f"{engine_name}://{user}:{password}@{host}{port_str}/{database}"


def get_engine(db_config):
    conn_str = build_connection_string(db_config)
    return create_engine(conn_str)


def execute_query(engine, sql, params=None):
    with engine.connect() as conn:
        result = conn.execute(text(sql), params or {})
        columns = list(result.keys())
        rows = result.fetchall()
        return columns, [dict(zip(columns, row)) for row in rows]
