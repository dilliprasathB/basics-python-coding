import math
binary=1010
decimal=0
i=0

while binary>0:
    digit=binary%10
    decimal=decimal+digit*math.pow(2,i)
    binary=binary//10
    i+=1

print(decimal)
    
