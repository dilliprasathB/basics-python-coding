#square root of the number


def squarerootofnumber (n):
    lo=1
    hi=n
    res=1

    while lo<=n:
        mid=lo+(hi-lo)//2

        if mid*mid<=n:
            res=mid
            lo=mid+1
        else:
            hi=mid-1

    return res
