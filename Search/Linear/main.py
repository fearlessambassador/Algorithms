


def linear_search(vals: list, x: int) -> str:
    """ Linear search algorithm.

    Parameters:
    vals (list): set of numbers to search in.
    x (int): the value we are looking for.

    Returns:
    string: A formatted string of the searched value and the
    index where it is placed in the list OR Element not found.
    """
    n = len(vals)
    for i in range(0, n):
        if (vals[i] == x):
            return 'Found value: {value} at index: {index}.' \
            .format( value = str(x), index = str(i) )
        
    return 'Element not found.'

arr = [1, 3, 5, 8, 9, 13]
x = 13
result = linear_search(arr, x)
print(result)