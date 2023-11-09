
#the given array must be sorted!

def binary_search(arr,element,low,high):

    import math

    ind = math.floor((high+low)/2)

    if arr[ind] == element : return ind
    elif arr[ind]<element : return binary_search(arr,element,ind,high)
    else : return binary_search(arr,element,0,ind)
