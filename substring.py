#array subset

def issubset(a,b):
    hash=set(a)
    for num in b:
        if num not in hash:
            return False
    return True
a=[1,2,3,4,5,6]
b=[1,2,8]
print("array subset is",issubset(a,b))
