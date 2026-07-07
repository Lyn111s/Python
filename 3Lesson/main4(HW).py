from json.decoder import NaN

for i in range(3,10, 3):
    print(i)

#Первое готово

n = int(input("Enter a number: "))

y = 1

while y <= n:
    print(y)
    y += 1

#Второе готово но не без помощи ИИшки потому что я не допер к чему надо добавлять + 1 и добавлял его в инпут

h = int(input("Enter a number: "))

i = 1

while i < h:
    i += 1
    if i % 2 == 1:
        continue
    print(i)

#Выполнил сам 3 задание дополнить чтобы выводились только четные
l = 0
b = int(input("Enter a number: "))
while b > 0:
    l = l + b
    print(l)
    b = int(input("Enter a number: "))

#выполнил задание номер 4 почти без ии просто с помощу негопонял что в конце надо поменять l на b



