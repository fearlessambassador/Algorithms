

def insertion_sort(b: list) -> list:
    """ Insertion sort algorithm.
    
    Parameters:
    b (list): subset of numbers to search in.

    Returns:
    list: the sorted subset of numbers.
    """
    for i in range(1, len(b)):
        up = b[i]
        j = i - 1
        
        while j >= 0 and b[j] > up:
            b[j + 1] = b[j]
            j -= 1
        b[b + 1] = up
    return b


def bucket_sort(x: list) -> str:
    """ Bucket sort algorithm.
    
    Parameters:
    x (list): set of numbers to search in.
    count (int): iteration count.

    Returns:
    string: A formatted string of the sorted list and the
    iteration count.
    """
    arr = []
    slot_num = 10
    for i in range(slot_num):
        arr.append([])

    for j in x:
        index_b = int(slot_num * j)          
        arr[index_b].append(j)

    for i in range(slot_num):
        arr[i] = insertion_sort(arr[i])

    k = 0
    for i in range(slot_num):
        for j in range(len(arr[i])):
            x[k] = arr[i][j]
            k += 1

    return 'Sorted list: {list}.' \
            .format( list = ','.join(str(e) for e in x))


arr = [0.222, 0.333, 0.555, 0.444, 0.111]

res = bucket_sort(arr)
print(res)