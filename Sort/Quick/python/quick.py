class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + ' - ' + str(self.age)
        

def partition(array, start, end, compare_func):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and  compare_func(array[high], pivot):
            high = high - 1

        while low <= high and not compare_func(array[low], pivot):
            low = low + 1
        
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[start], array[high] = array[high], array[start]

    return high

def quick_sort(array, start, end, compare_func):
    if start >= end:
        return
    
    p = partition(array, start, end, compare_func)
    quick_sort(array, start, p-1, compare_func)
    quick_sort(array, p+1, end, compare_func)

p1 = Person("Dave", 21)
p2 = Person("Jane", 58)
p3 = Person("Matthew", 43)
p4 = Person("Mike", 21)
p5 = Person("Tim", 10)
p6 = Person("Tim2", 100)

array = [p1, p2, p3, p4, p5, p6]

quick_sort(array, 0, len(array) - 1, lambda x, y: x.age > y.age)

for person in array:
    print(person)