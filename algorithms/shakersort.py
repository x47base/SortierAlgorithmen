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

def Shakersort(array: list, sort_option: int):
    """

    Sort Options:
    (1) Nachname
    (2) PLZ
    (3) Geburtsdatum (dd.mm.yyyy)
    (4) Vermögen (Decimal)
    """

    options = [2, 4, 5, 6]  # CSV Header Positions of the Options
    option = options[sort_option - 1]

    n = len(array)
    
    def swap(x: int, y: int):
        _x, _y = array[x], array[y]
        array[y] = _x
        array[x] = _y

    def shake():
        pass
    
    pass

if __name__ == "__main__":
    data = read_data()
    Shakersort(data, 2)
    print(data)
