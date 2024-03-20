import csv
import datetime


def read_data(file: str = "SortSmall.txt", seperator: str = ","):
    """

    Read Data froma a CSV File
    """
    rows = []
    with open(f"./data/{file}", "r") as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            to_int = [0, 4]
            to_date = [5]
            to_float = [6]

            for i in to_int:
                row[i] = int(row[i])

            for i in to_date:
                day_month_year = row[i].split(".")
                row[i] = datetime.date(
                    day=int(day_month_year[0]),
                    month=int(day_month_year[1]),
                    year=int(day_month_year[2]),
                )

            for i in to_float:
                row[i] = float(row[i])

            rows.append(row)
        file.close()
    return rows


if __name__ == "__main__":
    data = read_data()
    print(data)
