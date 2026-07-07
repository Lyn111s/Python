#5 Задание3
l = 0
b = 0
for a in range(1,11):
    l = int(input("Enter a number: ", ))
    if l <= 0:
        print("без негатива")
        break
    b = b + l
    print(a ,b)
