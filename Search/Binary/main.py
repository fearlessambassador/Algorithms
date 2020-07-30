


def binary_search(arr: list, l: int, r: int, x: int) -> str:
    """ Binary search algorithm. 
    
    Parameters:
    arr (list): set of numbers to search in.
    l (int): first index.
    r (int): length of the arr list.
    x (int): the value we are looking for.

    Returns:
    string: A formatted string of the searched value and the
    index where it is placed in the list OR Element not found.
    """

    if r >= l:

        # Mid point.
        mid = l + (r - l) // 2

        # If middle element of array is the
        # searched element.
        if arr[mid] == x:
            return 'Found value: {value} at index: {index}.' \
            .format( value = str(x), index = str(mid) )

        # Middle elem is greater than the searched value.
        elif arr[mid] > x:
            return binary_search(arr, l, mid - 1, x)

        # Middle elemenet is smaller than the searched value.
        else:
            return binary_search(arr, mid + 1, r, x)

    # Search finished, value not present.
    else:
        return 'Element not found.'


arr = [2, 3, 4, 10, 30, 40, 55]
n = len(arr) - 1

result = binary_search(arr, 0, n, 10)
print (result)