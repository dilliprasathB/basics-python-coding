'''Given two arrays a[] and b[] of equal size, the task is to find whether the elements in the arrays are equal.

Two arrays are said to be equal if both contain the same set of elements, arrangements (or permutations) of elements may be different though.

Note: If there are repetitions, then counts of repeated elements must also be the same for two arrays to be equal'''

def checkequal(a,b):
    if len(a) != len(b):
        return false
    return sorted(a)==sorted(b)

    if a==b:
        print("true")

    else:
        print("false")

