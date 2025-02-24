print("Enter the data seperated by commas: ", end="")

data= input().split(",")

"""for i in range(len(data)):
    if data[i].isdigit():
        data[i]=int(data[i])
    else:
        data[i]=str(data[i])"""

x = str(input("Enter the no to be searched: "))
if x in data:
    print("Num found at index: ", data.index(x))
else:
    print("Num not found")