from linkedlist import LinkedList
from bubblesort import bubble_sort
from linearsearch import linear_search

def linkedlist_to_list(linked_list):
    """Convert LinkedList to a Python list."""
    current = linked_list.head
    result = []
    while current:
        result.append(current.data)
        current = current.next
    return result

def list_to_linkedlist(lst):
    """Convert a Python list to LinkedList."""
    linked_list = LinkedList()
    for item in lst:
        linked_list.append(item)
    return linked_list

# Example usage
if __name__ == "__main__":
    # LinkedList example
    ll = LinkedList()
    ll.append(3)
    ll.append(1)
    ll.append(4)
    ll.append(2)
    print("Original LinkedList:")
    ll.print_list()  # Output: 3 -> 1 -> 4 -> 2 -> None

    # Convert LinkedList to list
    arr = linkedlist_to_list(ll)
    print("\nConverted to list:", arr)  # Output: [3, 1, 4, 2]

    # Bubble Sort the list
    bubble_sort(arr)
    print("Sorted list:", arr)  # Output: [1, 2, 3, 4]

    # Convert sorted list back to LinkedList
    sorted_ll = list_to_linkedlist(arr)
    print("Sorted LinkedList:")
    sorted_ll.print_list()  # Output: 1 -> 2 -> 3 -> 4 -> None

    # Linear Search in the sorted list
    target = 3
    result = linear_search(arr, target)
    if result != -1:
        print(f"\nElement {target} found at index {result}")
    else:
        print(f"\nElement {target} not found")