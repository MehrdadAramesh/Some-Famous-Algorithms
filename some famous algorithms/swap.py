#swap two elements in a list

def swap(arr,i,j):
    
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

    return arr