

def binary_search(arr, l, r, x):

    if r >= l:

        mid = l + (r -l) // 2
        mid = int(mid)

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binary_search(arr, l, mid - 1, x)

        else:
            return binary_search(arr, mid + 1, r, x)

    else:
        return -1


def exponential_search(arr, n, x):

    if arr[0] == x:
        return 0
    

    i = 1
    while i < n and arr[i] <= x:
        i = i * 2
    
    return binary_search(arr, i / 2, min(i, n), x)

arr = [2, 3, 4, 10, 40, 55]
n = len(arr)
x = 4
result = exponential_search(arr, n, x)
if (result == -1):
    print("Element is not present in array") 
else:
    print("Element is present at index", result)