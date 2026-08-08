'''
1! =1
2! = 2x1
3! =3x2x1
4! = 4x3x2x1
5! = 5x4x3x2x1

'''
def fact(n):
    if(n==0 or n==1):
        return 1
    return n * fact(n-1)


n = int(input("Enter number for factorial: "))
ans = fact(n)
print(f"The factorial of {n} is {ans}")