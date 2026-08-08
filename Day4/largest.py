def Largest(num1, num2, num3):
    ans = max(num1,num2,num3)
    return ans

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))


Lar=Largest(a,b,c)
print(f"The largest between {a,b,c} is {Lar}")