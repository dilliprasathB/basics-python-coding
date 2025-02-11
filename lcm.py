def lcm_value(x,y):
    if x>y:
        greater=x
    else:
        greater=y

    while(True):
        if greater%x==0 and greater%y==0:
            lcm=greater
            break
        greater+=1

    return lcm
x=12
y=14
print(lcm_value(x,y))
