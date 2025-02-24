def fac(x):
    if x==1:
        return 1
    else:
     return x*fac(x-1)
    
x=int(input("Enter the number: "))
print("Factorial of ", x, "is: ", fac(x))