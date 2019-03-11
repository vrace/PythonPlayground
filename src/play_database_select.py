#!/usr/bin/env python3
import sqlite3


def dump_data(conn):
    row_count = 0
    cursor = conn.execute("SELECT * FROM suppliers")
    for row in cursor.fetchall():
        print(f"{row_count + 1:08}\t{row}")
        row_count += 1
    print()
    print(f"{row_count} rows dumped.")


def main():
    conn = sqlite3.connect("../res/supplier.db")
    dump_data(conn)


if __name__ == "__main__":
    main()
