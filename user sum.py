n=int(input("enter num"))
i=0
sum=0
while n>0:
    sum=sum+(n%10)
    n=n//10
    i=i+1
print(sum)
   