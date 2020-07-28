


def bubble_sort(arr):
    """ Bubble sort algorithm.
    
    Parameters:
    arr (list): set of numbers to search in.

    Returns:
    string: A formatted string of the sorted list and the
    iteration count.
    """
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        if swapped == False:
            return 'Sorted list: {list}.' \
            .format( list = ','.join(str(e) for e in arr))      

arr = [1, 4, 5, 9, 99, 3]
result = bubble_sort(arr)

print(result)