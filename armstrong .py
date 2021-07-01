n=int(input("enter num"))
sum=0
a=n
while a>0:
    b=a%10
    sum=sum+b**3
    a=a//10
if n==sum:
    print(n,"arm strong")
else:
    print(n,"not armstrong")