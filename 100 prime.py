n=1
while n<=100:
    c=0
    i=1
    while i<=n:
        if n%i==0:
            c=c+1
        i=i+1
    if c==2:
        print(n)
    n=n+1