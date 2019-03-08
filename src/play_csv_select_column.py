#!/usr/bin/env python3
import csv


src_file = "../res/sample.csv"
out_file = "../res/select_column_out.csv"


def transfer(in_csv, out_csv):
    header = next(in_csv)
    out_csv.writerow(header)
    row_count = 0
    for row in in_csv:
        out_csv.writerow(row)
        row_count += 1
    return row_count


def main():
    with open(src_file) as in_fp:
        in_csv = csv.reader(in_fp)
        with open(out_file, "w") as out_fp:
            out_csv = csv.writer(out_fp)
            row_count = transfer(in_csv, out_csv)
    print(f"{row_count} rows transferred.")


if __name__ == "__main__":
    main()
