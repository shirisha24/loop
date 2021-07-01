n=input("enter string")
a=[]
b=" "
i=0
while i<len(n):
    if n[i]==" ":
        a.append(b)
        b=" "
    else:
        b=b+n[i]
    i=i+1
if b:
    a.append(b)
print(a)