

def binary_search(arr, l, r, x):
    """ Binary search algorithm. 
    
    Parameters:
    arr (list): set of numbers to search in.
    l (int): first index.
    r (int): length of the arr list.
    x (int): the value we are looking for.

    Returns:
    int: the index of the searched element, or
    -1 if not found.
    """
    if r >= l:

        mid = l + (r -l) // 2
        mid = int(mid)

        if arr[mid] == x:
            return 'Found value: {value} at index: {index}.' \
                .format( value = str(x), index = str(mid) )

        elif arr[mid] > x:
            return binary_search(arr, l, mid - 1, x)

        else:
            return binary_search(arr, mid + 1, r, x)

    else:
        return -1


def exponential_search(arr, n, x):
    """ Exponential search algorithm. 
    
    Parameters:
    arr (list): set of numbers to search in.
    n (int): lenght of the list.
    x (int): the value we are looking for.

    Returns:
    string: A formatted string of the searched value and the
    index where it is placed in the list OR Element not found.
    """
    if arr[0] == x:
        return 'Found value: {value} at index: {index}.' \
            .format( value = str(x), index = str(0) )
    

    i = 1
    while i < n and arr[i] <= x:
        i = i * 2
    
    return binary_search(arr, i / 2, min(i, n), x)

arr = [2, 3, 4, 10, 40, 55]
n = len(arr)
x = 55
result = exponential_search(arr, n, x)
print(result)
