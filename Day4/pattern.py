def Pattern(n):
    if(n==0):
        return
    print("*" * n)
    Pattern(n-1)
    
num = int(input("Enter a number: "))
Pattern(num)