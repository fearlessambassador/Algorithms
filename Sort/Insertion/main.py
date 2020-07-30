def insertion_sort(arr: list) -> str:
    """ Insertion sort algorithm.
    
    Parameters:
    arr (list): subset of numbers to search in.

    Returns:
    list: the sorted subset of numbers.
    """
    for i in range(1, len(arr)):

        key = arr[i]
        j = i-1
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    return 'Sorted list: {list}.' \
            .format( list = ','.join(str(e) for e in arr))


arr = [12, 11, 13, 5, 6] 
res = insertion_sort(arr)
print(res) 

