import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        prog="python-sql-reporter",
        description="Extrae datos de SQL y genera reportes Excel",
    )
    subparsers = parser.add_subparsers(dest="command")

    run_parser = subparsers.add_parser("run", help="Ejecutar queries y generar Excel")
    run_parser.add_argument(
        "--query", "-q", help="Ejecutar solo una query especifica"
    )
    run_parser.add_argument(
        "--output", "-o", default="report.xlsx", help="Archivo Excel de salida"
    )
    run_parser.add_argument(
        "--config", "-c", default="reports.yaml", help="Archivo de configuracion YAML"
    )

    subparsers.add_parser("list", help="Listar queries configuradas")

    return parser.parse_args()
