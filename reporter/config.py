import yaml


def load_config(path="reports.yaml"):
    try:
        with open(path, "r") as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        print(f"Error: no se encontro {path}")
        raise


def get_databases(config):
    return config.get("databases", {})


def get_queries(config):
    return config.get("queries", {})
