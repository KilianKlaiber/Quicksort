# Improving Quicksort using parallelprocessing

from concurrent.futures import ProcessPoolExecutor


def quicksort(arr):
    """Sorts an array using the Quicksort algorithm."""
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]  # Choose the middle element as the pivot
        left = [x for x in arr if x < pivot]  # Elements less than the pivot
        middle = [x for x in arr if x == pivot]  # Elements equal to the pivot
        right = [x for x in arr if x > pivot]  # Elements greater than the pivot
        
          # Use ProcessPoolExecutor to process each half in parallel
        with ProcessPoolExecutor(max_workers=2) as executor:
            # submit tasks to be executed
            futures = [
                executor.submit(quicksort, left),
                executor.submit(quicksort, right),
            ]
            # Collect the results from these tasks
            results = [future.result() for future in futures]
            
        return results[0] + middle + results[1]  # Recursively apply quicksort

# Example usage
if __name__ == "__main__":
    unsorted_array = [3, 6, 8, 10, 1, 2, 1]
    sorted_array = quicksort(unsorted_array)
    print("Sorted array:", sorted_array)
