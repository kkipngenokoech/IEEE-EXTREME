# linearsearch.py

def linear_search(arr, target):
    """
    Perform a linear search for the target in the given list.

    Parameters:
    arr (list): The list to search through.
    target: The value to search for.

    Returns:
    int: The index of the target if found, otherwise -1.
    """
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

# Example usage
if __name__ == "__main__":
    arr = [10, 23, 45, 70, 11, 15]
    target = 70
    result = linear_search(arr, target)
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found")