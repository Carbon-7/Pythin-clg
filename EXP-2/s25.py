print("Enter side 1: ", end="")
x = int(input())
print("Enter side 2: ", end="")
y = int(input())
print("Enter side 3: ", end="")
z = int(input())
if (x**2 == (y**2)+(z**2) or y**2 == (x**2)+(z**2) or z**2 == (x**2)+(y**2)):
    print("Right Angle Triangle")
else:
    print("Not a Right Angle Triangle")