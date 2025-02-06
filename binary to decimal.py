decimal=4
str binary=""
while decimal>0:
    digit=decimal%2
    binary=digit+binary
    decimal=decimal//2
print(binary)
