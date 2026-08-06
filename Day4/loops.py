l = [1,2,3,4,"Romeo", "Mayur", "Rahul"]

i = 0
while(i<len(l)):       #loop in list
    print(l[i])
    i += 1


for i in range(25):
    print(i)

for i in range(25):
    if(i==12):
        continue      #Continue the loop
    print(i)


    
for i in range(25):
    if(i==12):
        break           #break the loop
    print(i)