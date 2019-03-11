#!/usr/bin/env python3
import sqlite3


def prepare_table(conn):
    query = """
        CREATE TABLE sales(
            customer VARCHAR(20),
            product VARCHAR(40),
            amount FLOAT,
            date DATE
        );
    """
    conn.execute(query)
    conn.commit()


def prepare_data(conn):
    data = [
        ("Richard Lucas", "Notepad", 2.5, "2014-01-02"),
        ("Jenny Kim", "Binder", 4.15, "2014-01-15"),
        ("Svetlana Crow", "Printer", 155.75, "2014-02-03"),
        ("Stephen Randolph", "Computer", 679.4, "2014-02-20")
    ]
    query = "INSERT INTO sales VALUES (?, ?, ?, ?);"
    conn.executemany(query, data)
    conn.commit()


def update_data(conn):
    data = (5.2, "Jenny Kim")
    query = "UPDATE sales SET amount=? WHERE customer=?;"
    cursor = conn.execute(query, data)
    conn.commit()
    print(f"{cursor.rowcount} rows updated.")


def select_rows(conn):
    query = "SELECT * FROM sales;"
    cursor = conn.execute(query)
    for row_id, row_data in enumerate(cursor.fetchall()):
        print(f"{row_id:08}\t{row_data}")


def main():
    conn = sqlite3.connect(":memory:")
    prepare_table(conn)
    prepare_data(conn)
    print("Rows before update...")
    select_rows(conn)
    update_data(conn)
    print("Rows after update...")
    select_rows(conn)


if __name__ == "__main__":
    main()
