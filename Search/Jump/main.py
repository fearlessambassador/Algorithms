import math

def jump_search(arr: list, x: int) -> str:
    """ Jump search algorithm.
    
    Parameters:
    arr (list): set of numbers to search in.
    x (int): the value we are looking for.

    Returns:
    string: A formatted string of the searched value and the
    index where it is placed in the list OR Element not found.
    """

    n = len(arr) 
    # Define block size.
    step = math.sqrt(n)

    
    prev = 0
    i = int(min(step, n) - 1)
    # Find the block containing the element,
    # if containing.
    while arr[i] < x:
        prev = step
        step += math.sqrt(n)
        i = int(min(step, n)) - 1

        if prev >= n:
            return 'Element not found.'

    # Linear search for x in the block
    # begining with prev.
    while arr[int(prev)] < x: 
        prev += 1
    
        if prev == min(step, n): 
            return 'Element not found.'
    
    if arr[int(prev)] == x: 
        return 'Found value: {value} at index: {index}.' \
            .format( value = str(x), index = str(int(prev)) )

    return 'Element not found.'


arr = [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 
    34, 55, 89, 144, 233, 377, 610 ] 
x = 55

result = jump_search(arr, x) 
print(result)