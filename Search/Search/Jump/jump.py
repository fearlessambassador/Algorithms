

import math

def jump_search(vals, x):
    """ """

    # Length of the array.
    n = len(arr) 
    # Define block size.
    step = math.sqrt(n)

    # Find the block containing the element,
    # if containing.
    prev = 0

    i = int(min(step, n) - 1)
    while vals[i] < x:
        prev = step
        step += math.sqrt(n)
        i = int(min(step, n)) - 1

        if prev >= n:
            return 'Element not found.'

    # Linear search for x in the block
    # begining with prev.
    while vals[int(prev)] < x: 
        prev += 1
    
        if prev == min(step, n): 
            return 'Element not found.'
    
    if vals[int(prev)] == x: 
        return 'Found value: {value} at index: {index}.' \
            .format( value = str(x), index = str(int(prev)) )

    return 'Element not found.'


# Driver code to test function 
arr = [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 
    34, 55, 89, 144, 233, 377, 610 ] 
x = 555
  
# Find the index of 'x' using Jump Search 
result = jump_search(arr, x) 
print(result)