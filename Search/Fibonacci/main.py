def fibonacci_search(arr: list, val: int) -> str:
    """ Fibonacci search algorithm. 
    
    Parameters:
    arr (list): set of numbers to search in.
    val (int): the value we are looking for.

    Returns:
    string: A formatted string of the searched value and the
    index where it is placed in the list OR Element not found.
    """
    fibM_minus_2 = 0
    fibM_minus_1 = 1
    fibM = fibM_minus_1 + fibM_minus_2
    while (fibM < len(arr)):
        fibM_minus_2 = fibM_minus_1
        fibM_minus_1 = fibM
        fibM = fibM_minus_1 + fibM_minus_2

    index = -1
    while (fibM > 1):
        i = min(index + fibM_minus_2, (len(arr)-1))
        if (arr[i] < val):
            fibM = fibM_minus_1
            fibM_minus_1 = fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
            index = i

        elif (arr[i] > val):
            fibM = fibM_minus_2
            fibM_minus_1 = fibM_minus_1 - fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1

        else :
            return 'Found value: {value} at index: {index}.' \
                .format( value = str(val), index = str(i) )

    if(fibM_minus_1 and index < (len(arr)-1) and arr[index+1] == val):
        res = index+1
        return 'Found value: {value} at index: {index}.' \
            .format( value = str(val), index = str(res) )
            
    return 'Element not found.'

arr = [1,2,3,4,5,6,7,8,9,10,11]
res = fibonacci_search(arr, 1)
print(res)