#!/usr/bin/env python3
import csv


src_file = "../res/sample.csv"
out_file = "../res/select_row_out.csv"


def main():
    with open(src_file) as fp:
        reader = csv.reader(fp)
        with open(out_file, "w") as out_fp:
            writer = csv.writer(out_fp)
            rows_transferred = transfer(reader, writer)
    print(f"{rows_transferred} rows transferred.")


def transfer(in_csv, out_csv):
    header = next(in_csv)
    row_count = 0
    out_csv.writerow(header)
    for row in in_csv:
        if filter_row(row):
            out_csv.writerow(row)
            row_count += 1
    return row_count


def filter_row(row):
    supplier = row[0]
    try:
        cost = float(row[3].strip('$').replace(",", ""))
    except Exception as details:
        print(f"Error converting cost - {details}")
        return False
    return supplier == "Supplier Z" or cost > 300.0


if __name__ == "__main__":
    main()
