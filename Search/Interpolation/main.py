

def interpolation_search(vals: list, x: int) -> str:
    """ Basic interpolation search algorithm.
    
    Parameters:
    vals (list): set of numbers to search in.
    x (int): the value we are looking for.

    Returns:
    string: A formatted string of the searched value and the
    index where it is placed in the list OR Element not found.
    """

    # First item's ID.
    id_0 = 0
    # Last item's ID.
    id_n = (len(vals) - 1)

    while id_0 <= id_n and x >= vals[id_0] and x <= vals[id_n]:

        # Mid point.
        mid = id_0 + int(((float(id_n - id_0) / \
             (vals[id_n] - vals[id_0])) * (x - vals[id_0])))

        # Compare mid value with search val.
        if vals[mid] == x:
            return 'Found value: {value} at index: {index}.' \
            .format( value = str(x), index = str(mid) )

        if vals[mid] < x:
            id_0 = mid + 1

    return 'Element not found.'


l = [0, 2, 6, 11, 19, 27, 31, 45, 121]
result = interpolation_search(l, 19)
print(result)