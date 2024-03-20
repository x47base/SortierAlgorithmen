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

def Heapsort(array: list, sort_option: int):
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

    def heapify(arr: list, i: int, heap_size: int):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i

        if left < heap_size and arr[left][option] > arr[largest][option]:
            largest = left
        if right < heap_size and arr[right][option] > arr[largest][option]:
            largest = right

        if largest != i:
            swap(i, largest)
            heapify(arr, largest, heap_size)

    def build_max_heap(arr: list):
        for i in range(n // 2 - 1, -1, -1):
            heapify(arr, i, n)

    build_max_heap(array)
    for i in range(n - 1, 0, -1):
        swap(0, i)
        heapify(array, 0, i)

if __name__ == "__main__":
    data = read_data()
    Heapsort(data, 2)
    print(data)
