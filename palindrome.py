n=int(input("enter num"))
a=n
rev=0
while n>0:
    b=n%10
    rev=(rev*10)+b
    n=n//10
if (a==rev):
    print(a,"palindrome")
else:
    print(a,"not palindrome")


# anthoer model
n=int(input("enter num"))
a=0
r=0
while n>0:
    a=n%10
    r=r*10+a
    n=n//10
print(r)