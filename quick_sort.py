def quick_sort(arr):
    # partition the array and return the pivot index
    def partition(arr, low, high):
        pivot = arr[high]  # choosing the last element as the pivot
        i = low - 1
        
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]  # swap elements
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]  # swap pivot to correct position
        return i + 1
    
    # handle the recursion
    def quicksort(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)  # the pivot index
            quicksort(arr, low, pi - 1)  # sort elements before the pivot
            quicksort(arr, pi + 1, high)  # sort elements after the pivot
    
    # start the quicksort with the full array
    quicksort(arr, 0, len(arr) - 1)
    
    return arr