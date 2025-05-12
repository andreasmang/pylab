def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Track whether any swaps occur in this pass
        swapped = False
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap if out of order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no swaps, the array is sorted
        if not swapped:
            break
    return arr

# Example usage
if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", data)
    sorted_data = bubble_sort(data)
    print("Sorted array:", sorted_data)

