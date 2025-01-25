import random
import time

from selection_sort import selection_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
from heap_sort import heap_sort
from graph import plot_graph

# calculate the time for each sort
def run_sorting(arr, sort_function, num_runs):
    times = []
    
    for _ in range(num_runs):
        start_time = time.time()
        sort_function(arr)
        end_time = time.time()
        times.append(end_time - start_time)
    
    return times

# print average times for the chosen sorting algorithm
def print_average_times(arr, sort_function, num_runs):
    print(f"Unsorted array (first 10 elements): {arr[:10]}")
    sorting_time = run_sorting(arr, sort_function, num_runs)

    sorted_array = arr[:]
    print(f"Sorted array (first 10 elements): {sorted_array[:10]}")
    ascending_sort_time = run_sorting(sorted_array, sort_function, num_runs)

    descending_array = sorted_array[::-1]
    print(f"Descending array (first 10 elements): {descending_array[:10]}")
    descending_sort_time = run_sorting(descending_array, sort_function, num_runs)

    # calculate and print the average time for sorting
    average_time = sum(sorting_time) / num_runs
    ascending_time = sum(ascending_sort_time) / num_runs
    descending_time = sum(descending_sort_time) / num_runs

    print(f"Average time to sort the array: {average_time:.6f} seconds")
    print(f"Average time to sort the sorted array in ascending order: {ascending_time:.6f} seconds")
    print(f"Average time to sort the descending array: {descending_time:.6f} seconds\n")

    return average_time, ascending_time, descending_time

def main():

    num_runs = 30
    array_sizes = [500, 1000, 1500, 2000, 2500]
    # for quick sort due to recursion depth limit
    # array_sizes = [500, 600, 700, 800, 900, 1000]

    average_times = []
    ascending_times = []
    descending_times = []

    print("Choose the sorting algorithm:")
    print("1. Selection Sort")
    print("2. Insertion Sort")
    print("3. Merge Sort")
    print("4. Quick Sort")
    print("5. Heap Sort")

    choice = input("Enter number: ").strip()

    if choice == '1':
        sort_function = selection_sort
    elif choice == '2':
        sort_function = insertion_sort
    elif choice == '3':
        sort_function = merge_sort
    elif choice == '4':
        sort_function = quick_sort
    elif choice == '5':
        sort_function = heap_sort
    else:
        print("Invalid choice.")

    for size in array_sizes:
        arr = [random.randint(1, 10000) for _ in range(size)]
        print(f"Input size: {size}")
        avg_time, asc_time, desc_time = print_average_times(arr, sort_function, num_runs)
        average_times.append(avg_time)
        ascending_times.append(asc_time)
        descending_times.append(desc_time)

    plot_graph(sort_function, array_sizes, average_times, ascending_times, descending_times)

if __name__ == "__main__":
    main()
