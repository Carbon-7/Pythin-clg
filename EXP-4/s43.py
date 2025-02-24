print("Enter a string: ", end="")
x=str(input())

if((x == x[::-1]) == True):
    print("palindrome")
else:
    print("not a palindrome")