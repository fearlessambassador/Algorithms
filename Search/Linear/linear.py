


def linear_search(arr, n, x):

    for i in range(0, n):
        if (arr[i] == x):
            return i
        
    return -1

arr = [1, 3, 5, 8, 9, 13]
n = len(arr)
x = 13
result = linear_search(arr, n, x)
if (result == -1):
    print("Element is not present in array") 
else:
    print("Element is present at index", result)