import csv

def read_data(file: str = "SortSmall.txt", seperator: str = ","):
    rows = []
    with open(f"./data/{file}", 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            rows.append(row)
        file.close()
    return rows

if __name__ == "__main__":
    data = read_data()
    print(data)