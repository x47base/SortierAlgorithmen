from algorithms.quicksort import Quicksort
from algorithms.bubblesort import Bubblesort
from algorithms.heapsort import Heapsort
from reader import read_data

import time

def main():
    data = read_data(file="SortMedium.txt")
    # Options:     (1) Nachname    (2) PLZ    (3) Geburtsdatum (dd.mm.yyyy)    (4) Vermögen (Decimal)
    option = 1
    
    # Quicksort
    print("-- Quicksort --")    
    start = time.time()
    Quicksort(data, option)
    end = time.time()
    quicksort_time = end - start
    print(f"{quicksort_time:.9f} Sekunden")
    
    # Bubblesort
    print("-- Bubblesort --")
    start = time.time()
    Bubblesort(data, option)
    end = time.time()
    bubble_time = end - start
    print(f"{bubble_time:.9f} Sekunden")
    
    # Heapsort
    print("-- Heapsort --")
    
    # Another Sort Algorithm
    print("-- Another Sort Algorithm --")
    

if __name__ == "__main__":
    main()
