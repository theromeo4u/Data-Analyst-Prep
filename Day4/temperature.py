def cel_fer(f):
    temp = 5*(f-32)/9
    return temp


temperature = int(input("Enter temperature in Feranhiet: "))
ans = cel_fer(temperature)
print(f"{temperature} is {round(ans,2)} celcius")