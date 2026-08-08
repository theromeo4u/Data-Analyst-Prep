def Inch_to_cm(num):
    return num*2.54


n = int(input("Enter length in Inch: "))
ans = Inch_to_cm(n)
print(f"{n} Inch is = {ans} cms")