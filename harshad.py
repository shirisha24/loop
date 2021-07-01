# number is divisible by the sum of its then it will be known as harshad number
n=int(input("enter num"))
sum=0
a=n
while a>n:
    b=a%10
    a=a//10
    sum=sum+b
if sum%n==0:
    print(n,"harshad num")

else:
    print(n,"not harshad number")