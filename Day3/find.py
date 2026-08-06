l = []
num = int(input("Enter a number: "))
l.append(num)
num = int(input("Enter a number: "))
l.append(num)
num = int(input("Enter a number: "))
l.append(num)
num = int(input("Enter a number: "))
l.append(num)

find = int(input("Enter number to check: "))

if(find in l):
    print(f"{find} is present in list")
else:
    print(f"{find} is not present")