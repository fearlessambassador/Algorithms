def heapify(arr: list, n: int, i: int)-> list:
    """ Heapify the given list.
    
    Parameters:
    arr (list): set of numbers to search in.
    n (int): lenght of the list.
    i (int): root candidate.

    Returns:
    list: a heapified list.
    """
    largest = i # Root.
    left = 2 * i + 1    
    right = 2 * i + 2
  
    # If left child exists and larger than root.
    if left < n and arr[i] < arr[left]: 
        largest = left
  
    # If right child exists and larger than root.
    if right < n and arr[largest] < arr[right]: 
        largest = right
  
    # If root is not the largest.
    if largest != i: 
        arr[i], arr[largest] = arr[largest], arr[i] 
        # Heapify the root. 
        heapify(arr, n, largest) 

    return arr
  

def heap_sort(arr: list) -> str: 
    """ Heap sort algorithm.
    
    Parameters:
    arr (list): set of numbers to search in.

    Returns:
    string: A formatted string of the sorted list and the
    iteration count.
    """
    n = len(arr) 
    # Build max heap.
    arr = max_heap(arr, n//2 - 1, n)
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] 
        arr = heapify(arr, i, 0) 

    return 'Sorted list: {list}.' \
            .format( list = ','.join(str(e) for e in arr))   

def max_heap(arr: list, i: int, n:  int) -> list:
    """ Build max heap (recursive).
    
    Parameters:
    arr (list): set of numbers to search in.
    i (int): iteration count.
    n (int): half of the list minus 1.

    Returns:
    list: Max heaped list.
    """
    if i >= 0:
        i -= 1
        arr = heapify(arr, n, i) 
        max_heap(arr, i, n)
    
    return arr


arr = [ 12, 11, 9, 13, 5, 6, 7, 72, 73] 

result = heap_sort(arr)
print(result)
