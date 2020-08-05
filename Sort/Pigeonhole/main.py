def pigeonhole_sort(a): 
    """ Pigeonhole sort algorithm.
    
    Parameters:
    a (list): set of numbers to search in.

    Returns:
    string: A formatted string of the sorted list.
    """

    lowest = min(a) 
    highest = max(a) 
    # Size of the pigeonholes.
    size = highest - lowest + 1
  
    holes = [0] * size 
  
    # Fill the pigeonholes. 
    for x in a: 
        holes[x - lowest] += 1
  
    # Insert the elems back to the original list. 
    i = 0
    for count in range(size): 
        while holes[count] > 0: 
            holes[count] -= 1
            a[i] = count + lowest 
            i += 1
    
    return 'Sorted list: {list}.' \
            .format( list = ','.join(str(e) for e in a))  
              
  
a = [0, 8, 3, 2, 7, 4, 6, 8, 12, 47] 
  
res = pigeonhole_sort(a) 
print(res) 