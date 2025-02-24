x=int(input())
y=int(input())
z=int(input())
if(x>y and x>z):
    print(x, "is the largest")
elif(y>x and y>z):
    print(y, "is the largest")
else:
    print(z, "is the largest")