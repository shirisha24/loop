n=int(input("enter num"))
a=n
sum=0
while n>0:
    i=1
    f=1
    b=n%10
    while i<=b:
        f=f*i
        i=i+1
    sum=sum+f
    n=n//10
if sum==a:
    print("strong num")
else:
    print("not strong number")