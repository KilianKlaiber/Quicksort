# Standard Quicksort Algorithm


def quicksort(arr):
    """Sorts an array using the Quicksort algorithm."""
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]  # Choose the middle element as the pivot
        left = [x for x in arr if x < pivot]  # Elements less than the pivot
        middle = [x for x in arr if x == pivot]  # Elements equal to the pivot
        right = [x for x in arr if x > pivot]  # Elements greater than the pivot
        return quicksort(left) + middle + quicksort(right)  # Recursively apply quicksort

# Example usage
if __name__ == "__main__":
    unsorted_array = [3, 6, 8, 10, 1, 2, 1]
    sorted_array = quicksort(unsorted_array)
    print("Sorted array:", sorted_array)
