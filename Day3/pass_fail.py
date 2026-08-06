phy = int(input("Enter physics marks %: " ))
chem = int(input("Enter physics marks %: " ))
maths = int(input("Enter physics marks %: " ))

total = (phy+chem+maths)/3
if(phy>=33 and chem>=33 and maths>=33 and total>=40):
    print("Congratulations you are pass")

else:
    print("Try Next year ")
print(total)