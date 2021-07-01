n=int(input("enter num"))
i=1
while i<=n:
    if i%10==0:
        print("#")
    elif i%3==0:
        print("*")
    else:
        print(i)
    i=i+1