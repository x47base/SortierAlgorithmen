
def Quicksort(liste):
    def partition(arr, low, high):
        pivot = arr[high][2]
        i = low - 1
        for j in range(low, high):
            if arr[j][2] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quicksort_for_second_entry(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quicksort_for_second_entry(arr, low, pi - 1)
            quicksort_for_second_entry(arr, pi + 1, high)


    quicksort_for_second_entry(liste, 0, len(liste) - 1)

    # Ausgabe der sortierten Liste
    for zeile in liste:
        print(zeile)