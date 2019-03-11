#!/usr/bin/env python3
import csv
import sqlite3


def create_table(conn):
    sql = """
        CREATE TABLE IF NOT EXISTS suppliers(
            supplier_name VARCHAR(20),
            invoice_number VARCHAR(20),
            part_number VARCHAR(20),
            cost FLOAT,
            purchase_date DATE
        );
    """
    conn.execute(sql)
    conn.commit()


def dump_from_csv(in_csv, conn):
    next(in_csv)
    for row in in_csv:
        conn.execute("INSERT INTO suppliers VALUES (?, ?, ?, ?, ?);", row)
    conn.commit()


def main():
    conn = sqlite3.connect("../res/supplier.db")
    create_table(conn)
    with open("../res/sample.csv") as in_fp:
        in_csv = csv.reader(in_fp)
        dump_from_csv(in_csv, conn)


if __name__ == "__main__":
    main()
