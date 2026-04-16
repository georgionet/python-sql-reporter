#!/usr/bin/env python3
from reporter.cli import parse_args
from reporter.config import load_config, get_queries
from reporter.executor import run_query, run_all_queries
from reporter.excel import generate_report


def main():
    args = parse_args()

    if not args.command:
        print("Usa 'run' o 'list'. Ejecuta con --help para mas info.")
        return

    config = load_config(args.config if hasattr(args, "config") else "reports.yaml")

    if args.command == "list":
        queries = get_queries(config)
        if not queries:
            print("No hay queries configuradas.")
            return
        print("Queries configuradas:\n")
        for name, q in queries.items():
            db = q.get("database", "?")
            sheet = q.get("sheet_name", name)
            print(f"  {name:25s} DB: {db:15s} Sheet: {sheet}")
        print()
        return

    if args.command == "run":
        config_path = getattr(args, "config", "reports.yaml")
        config = load_config(config_path)
        output = getattr(args, "output", "report.xlsx")
        query_name = getattr(args, "query", None)

        if query_name:
            result = run_query(config, query_name)
            if result:
                generate_report({result[0]: result[1]}, output)
        else:
            results = run_all_queries(config)
            if results:
                generate_report(results, output)
            else:
                print("No se ejecutaron queries.")


if __name__ == "__main__":
    main()
