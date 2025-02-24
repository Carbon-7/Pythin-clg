print("Enter the numbers separated by comma: ", end="")
nums=list(map(int,input().split(",")))
print("Sum of the number from list", nums ,"is: "  , end="")
print(max(nums))