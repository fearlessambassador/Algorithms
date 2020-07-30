class Languages:
    """ Class to create language instances.

    Args:
    name (str): name of the language.
    year (int): year of creation.
    authors (str): author(s) of the language.
    """
    def __init__(self, name: str, year: int, authors: str):
        self.name = name
        self.created_year = year
        self.authors = authors

    def __str__(self):
        return str.format("Created year: {}, Name: {}, Created by: {}", \
            self.created_year, self.name, self.authors)

def merge(arr: list, l_index: int, r_index: int, \
    mid: int, comparison_func) -> list:

    l_copy = arr[l_index : mid+1]
    r_copy = arr[mid+1 : r_index+1]

    l_copy_index = 0
    r_copy_index = 0
    sorted_index = l_index

    while l_copy_index < len(l_copy) and r_copy_index < len(r_copy):

        if comparison_func(l_copy[l_copy_index], r_copy[r_copy_index]):
            arr[sorted_index] = l_copy[l_copy_index]
            l_copy_index += 1
        
        else:
            arr[sorted_index] = r_copy[r_copy_index]
            r_copy_index += 1
        
        sorted_index += 1

    while l_copy_index < len(l_copy):
        arr[sorted_index] = l_copy[l_copy_index]
        l_copy_index += 1
        sorted_index += 1

    while r_copy_index < len(r_copy):
        arr[sorted_index] = r_copy[r_copy_index]
        r_copy_index += 1
        sorted_index += 1


def merge_sort(arr: list, l_index: int, r_index: int, comparison_func):

    if l_index >= r_index:
        return

    mid = (l_index + r_index) // 2
    merge_sort(arr, l_index, mid, comparison_func)
    merge_sort(arr, mid + 1, r_index, comparison_func)
    merge(arr, l_index, r_index, mid, comparison_func)


lang_1 = Languages('IPL', 1954, 'Allen Newell, Cliff Shaw, and Herbert A. Simon')
lang_2 = Languages('Regional Assembly Language', 1951, 'David Wheeler')
lang_3 = Languages('FLOW-MATIC', 1955, 'Grace Hopper')
lang_4 = Languages('Autocode', 1952, 'Alick Glennie')

arr = [lang_1, lang_2, lang_3, lang_4]

merge_sort(arr, 0, len(arr) - 1, lambda lang1, lang2: lang1.created_year < lang2.created_year)
for lang in arr:
    print(lang)