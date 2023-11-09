
def insertion_sort(arr):

    n = len(arr)

    for i in range(n):

        k = i

        while arr[k]<arr[k-1] and k>0:

            temp = arr[k]
            arr[k] = arr[k-1]
            arr[k-1] = temp
            k -= 1

    return arr

#insertion sort without swaping

def insertion_sort_2(arr):

    n = len(arr)

    for i in range(1,n):

        y = arr[i]
        k = i-1

        while k>=0 and y<arr[k]:

            arr[k+1]  = arr[k]
            k -= 1

        arr[k+1] = y

    return arr





