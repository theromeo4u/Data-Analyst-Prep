marks={
    "Subodh":100,
    "mayur":95,
    "Rahul":90
}

print(marks, type(marks))
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Subodh": 99, "Suraj" : 98})
print(marks)
print(marks.get("Subodh"))