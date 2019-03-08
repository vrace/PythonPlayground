#!/usr/bin/env python3
import sqlite3


def main():
    con = sqlite3.connect(":memory:")
    query = """
    CREATE TABLE sales(
    customer VARCHAR(20),
    product VARCHAR(40),
    amount FLOAT,
    date DATE
    );
    """
    con.execute(query)
    con.commit()

    data = [
        ("Richard Lucas", "Notepad", 2.5, "2014-01-01"),
        ("Jenny Kim", "Binder", 4.15, "2014-01-15"),
        ("Svetlana Crow", "Printer", 155.75, "2014-02-03"),
        ("Stephen Randolph", "Computer", 679.4, "2014-02-20")
    ]

    statement = "INSERT INTO sales VALUES(?, ?, ?, ?)"
    con.executemany(statement, data)
    con.commit()

    cursor = con.execute("SELECT * FROM sales")
    rows = cursor.fetchall()

    row_count = 0
    for row in rows:
        print(row)
        row_count += 1

    print(f"Number of rows: {row_count}")


if __name__ == "__main__":
    main()
