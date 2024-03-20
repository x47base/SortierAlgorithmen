from algorithms.quicksort import Quicksort
from algorithms.bubblesort import Bubblesort
from algorithms.heapsort import Heapsort
from reader import read_data

import time

def main():
    data = read_data(file="SortMedium.txt")
    
    # Quicksort
    print("-- Quicksort --")    
    
    # Bubblesort
    print("-- Bubblesort --")
    start = time.time()
    Bubblesort(data, 2)
    end = time.time()
    bubble_time = end - start
    print(f"{bubble_time:.9f} Sekunden")
    
    # Heapsort
    print("-- Heapsort --")
    
    # Another Sort Algorithm
    print("-- Another Sort Algorithm --")
    

if __name__ == "__main__":
    main()
