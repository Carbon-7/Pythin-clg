print("Enter the numbers separated by comma: ", end="")
nums=list(map(int,input().split(",")))

um = len(nums)
mul=1

for i in range(um):
    mul=mul*nums[i]

print("Multiplication of the numbers in list", nums , "is: ", end="")    
print(mul)