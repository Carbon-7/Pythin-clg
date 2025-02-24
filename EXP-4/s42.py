
x= input("Enter a string: ")
y= input("Enter the character whose occurance you want to test: ").lower()

print("Length of string: ", len(x))

n=len(x)
a=0
b=0

for i in range(n):
    if(x[i].isupper()==True):
        a+=1
    elif(x[i].islower()==True):
        b+=1
    else:
        break
    
print("Upper case: ", a)
print("Lower case: ", b)

s1= x.lower()
z= s1.count(y)

print("occurance of",y,":", z) 