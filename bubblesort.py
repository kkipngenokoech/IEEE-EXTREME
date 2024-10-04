# bubblesort.py

def bubble_sort(arr):
    n = len(arr)
    for i in range(n): # Loop through the entire list
        # Track if any swaps are made in this pass
        swapped = False 
        for j in range(0, n-i-1): # Loop through the list up to the last unsorted element
            if arr[j] > arr[j+1]: # look at the current element and the next element
                # Swap if the element found is greater than the next element
                arr[j], arr[j+1] = arr[j+1], arr[j] # Swap the elements if they are in the wrong order
                swapped = True
        # If no swaps were made, the list is already sorted
        if not swapped:
            break

# Example usage
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr)
    bubble_sort(arr)
    print("Sorted array:", arr)