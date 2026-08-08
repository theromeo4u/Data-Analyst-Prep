def Sum(num):
    sum=0
    for i in range(num+1):
        sum += i
    return sum
    
num = int(input("Enter number: "))

ans = Sum(num)
print(f"Sum of {num} natural number is {ans}")