from algorithms.quicksort import Quicksort
from algorithms.bubblesort import Bubblesort
from algorithms.heapsort import Heapsort
from algorithms.shakersort import Shakersort
from reader import read_data

import sys
sys.setrecursionlimit(999999999)
import time

def main():
    _file="SortBig.txt"
    # Options:     (1) Nachname    (2) PLZ    (3) Geburtsdatum (dd.mm.yyyy)    (4) Vermögen (Decimal)
    option = 2
    
    # Quicksort
    print("-- Quicksort --")
    data = read_data(file=_file)    
    start = time.time()
    Quicksort(data, option)
    end = time.time()
    quicksort_time = end - start
    print(f"{quicksort_time:.9f} Sekunden")
    
    # Bubblesort

    print("-- Bubblesort --")
    data = read_data(file=_file)
    start = time.time()
    Bubblesort(data, option)
    end = time.time()
    bubble_time = end - start
    print(f"{bubble_time:.9f} Sekunden")
    
    # Heapsort
    print("-- Heapsort --")
    data = read_data(file=_file)
    start = time.time()
    Heapsort(data, option)
    end = time.time()
    heap_time = end - start
    print(f"{heap_time:.9f} Sekunden")
    
    # Another Sort Algorithm
    print("-- Another Sort Algorithm --")
    data = read_data(file=_file)
    start = time.time()
    Shakersort(data, option)
    end = time.time()
    heap_time = end - start
    print(f"{heap_time:.9f} Sekunden")

if __name__ == "__main__":
    main()
