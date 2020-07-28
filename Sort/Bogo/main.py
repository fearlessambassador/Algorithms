import random

def bogo_sort(arr, count):
    """ Bogo sort algorithm.
    
    Parameters:
    arr (list): set of numbers to search in.
    count (int): iteration count.

    Returns:
    string: A formatted string of the sorted list and the
    iteration count OR Element not found.
    """
    if is_sorted(arr) ==  False:
        random.shuffle(arr) # Shuffle the list.
        return bogo_sort(arr, count+1) # Recursion.

    return 'Sorted list: {list} at iteration count: {count}.' \
            .format( list = ','.join(str(e) for e in arr),  \
            count = count )

def is_sorted(arr):
    """ Iterate over the list to see if it already sorted.

    Parameters:
    arr: A list to sort.

    Returns:
    True or False.
    """
    n = len(arr)
    for i in range(0, n-1):
        if arr[i] > arr[i+1]:
            return False
        
    return True

a = [3, 2, 4, 1, 0, 5] 

res = bogo_sort(a, 0)
print(res)