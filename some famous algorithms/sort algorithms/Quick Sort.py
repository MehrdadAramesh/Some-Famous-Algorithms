from useful_funcs import swap

def partition(arr):

    pivot = arr[0]

    n = len(arr)
    j = n-1
    i = 1

    while i<=j :

        while (i<n and arr[i] < pivot):
            i += 1

        while (j>0 and arr[j] >= pivot):
            j -= 1

        if i<j : swap(arr,i,j)
    
    swap(arr,0,j)

    return arr , j



def quick_sort(arr):

    arr , ind = partition(arr)

    n = len(arr)


    arr_left = arr[:ind]
    arr_right = arr[ind+1:]

    if len(arr_left) > 1:

        arr_left = quick_sort(arr[:ind])

    if len(arr_right) > 1:

        arr_right = quick_sort(arr[ind+1:])

    

    return arr_left + [arr[ind]] + arr_right

