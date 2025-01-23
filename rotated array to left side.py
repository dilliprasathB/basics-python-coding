#rotated array to left side


def rotatedvalue(arr,d):
    n=len(arr)
    d%=n

    self.rotated(arr,0,d-1)
    self.rotated(arr,d,n-1)
    self.rotated(arr,0,n-1)

def rotated(self,arr,start,end):

    while start<end:
        arr[start],arr[end]=arr[end],arr[start]

        start+=1
        end-=1
    
