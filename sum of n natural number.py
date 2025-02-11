#sum of n natural num
def naturalno(n):
    sum=0
    x=1
    while(x<=n):
        sum=sum+x
        x=x+1
    return sum
n=5
print(naturalno(n))
