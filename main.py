"""
ETL-Query script
"""
import sys
import argparse
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import (
    insert_row,
    update_row,
    delete_row,
)


def handle_arguments(args):
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "action",
        choices=["extract", "load", "insert", "update", "delete"],
    )
    args = parser.parse_args(args[:1])
    if args.action == "insert":
        parser.add_argument("date")
        parser.add_argument("location")
        parser.add_argument("city")
        parser.add_argument("state")
        parser.add_argument("lat", type=float)
        parser.add_argument("lng", type=float)

    elif args.action == "update":
        parser.add_argument("city")
        parser.add_argument("date")

    elif args.action == "delete":
        parser.add_argument("city")

    return parser.parse_args(sys.argv[1:])


def main():
    args = handle_arguments(sys.argv[1:])

    if args.action == "extract":
        print("Extracting data...")
        extract()
    elif args.action == "load":
        print("Loading data to Databricks...")
        load()
    elif args.action == "insert":
        insert_row(
            args.date,
            args.location,
            args.city,
            args.state,
            args.lat,
            args.lng,
        )
    elif args.action == "update":
        update_row(args.city, args.date)
    elif args.action == "delete":
        delete_row(args.city)
    else:
        print(f"Unknown action: {args.action}")


if __name__ == "__main__":
    main()
    