#Third largest element in array

def thirdlargestvalue (arr):
    n=len(arr)
    arr.sort()

    for i n range(n-3,-2,-2):
        if arr[i]!=arr[n-1]:
            return arr[i]

    return arr
