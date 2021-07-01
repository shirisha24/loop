n=2
while n<=100:
    i=2
    c=0
    while i<=n:
        if n%i==0:
            c=c+1
        i=i+1
    if c==1:
        print(n)
    n=n+1