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