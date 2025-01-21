#find min & max value

def minmaxvalue (arr):

    if not arr:
        return None,None

    min_value=max_value=arr[0]   #0 is the index value

    for num in arr:

        if num<min_value:
            num=min_value

        elif num>max_value:
            num=max_value

    return(min_value,max_value)
