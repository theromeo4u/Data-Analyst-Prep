a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
d = int(input("Enter a number: "))

if(a>=b and a>=c and a>=d ):
    print(f"{a} is Greter")
elif(b>=c and b>=d):
    print(f"{b} is Greter")
elif(c>=d):
    print(f"{c} is Greter")
else:
    print(f"{d} is Greter")
