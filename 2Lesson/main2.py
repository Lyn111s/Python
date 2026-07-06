
bebe = input("напиши sheep")
age = int(input("напиши возраст овцы"))
print(bebe)
print(age)

if bebe == "sheep" and age < 18:
    print("beeeee young")
elif bebe == "sheep" and age > 18:
    print("beeeee old")
elif bebe == "sheep" or age < 18:
    print("at least it is a beeee or young")
elif bebe == "sheep" or age > 18:
    print("at least it is a beeee or old")
else:
    print("nope")