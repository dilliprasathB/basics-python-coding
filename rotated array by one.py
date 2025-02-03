#rotated array by one

def rotatedbyone (arr):
    n=len(arr)
    i,j=0,n-2
    while i<j:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1

    i,j=o,n-1
    while i<j:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1

