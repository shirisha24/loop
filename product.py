n=int(input("enter num"))
pro=1
a=n
while n>0:
    b=n%10
    pro=pro*b
    n=n//10
print(pro)