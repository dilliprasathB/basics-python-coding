#array search

def arraysearch (self,arr,x):
    for i in range(len(arr)):
        if arr[i]==x:
            return i
    return -1
