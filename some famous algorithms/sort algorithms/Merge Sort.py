import math


def merge(arr1,arr2):

    res = []

    arr1.append(math.inf)
    arr2.append(math.inf)

    max_len = max([len(arr1),len(arr2)])

    while arr1[0] != math.inf or arr2[0] != math.inf :

        if arr1[0] <= arr2[0]:

            res.append(arr1[0])
            arr1 = arr1[1:]

        else :

            res.append(arr2[0])
            arr2 = arr2[1:]
    
    if arr1[0] == math.inf: res += arr2[:-1]
    else : res += arr1[:-1]

    return(res)


def merge_sort(array):

    n = len(array)
    mid = math.floor(n/2)
    res = []

    arr_left = array[:mid]
    arr_right = array[mid:]

    if len(arr_left)>1:

        arr_left = merge_sort(arr_left)

    if len(arr_right)>1:
        
        arr_right = merge_sort(arr_right)

    res = merge(arr_left,arr_right)

    return res
        
    
