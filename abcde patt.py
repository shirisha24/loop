n=5
i=1
while n>=1:
    j=4
    while j>=n:
        print("",end="")
        j=j-1
    k=i
    while k<=5:
        print(chr(64+n),end=" ")
        k=k+1
    print()
    n=n-1
    i=i+1

# abc pattern
n=1
i=1
while n<=5:
    j=4
    while j>=n:
        print(" ",end=" ")
        j=j-1
    k=1
    while k<=i:
        print(chr(64+n),end=" ")
        k=k+1
    print()
    n=n+1
    i=i+2
