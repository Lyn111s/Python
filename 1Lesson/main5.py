A = 3
B = 4
answerPlus = A + B
answerMinus = A - B
answerSquare = A ** B
print(answerPlus)
print(answerMinus)
print(answerSquare)

print("Особые команды по типу += -=")
A = 3
A += 5
print(A)
A -= 5
print(A)
print("Виды деления")
print(10 / 3)
print(10 // 3)
print("Проверка на четность числа")
num2 = 9
num1 = 8
print(num2 % 2)
print(num1 % 2)
# в консоли ответ num2 = 1 не четное, а вот num1 будет равна 0 и будет четным числом так как ничего не осталось
print("Это преобразование с флот в целое число")
print(int(3/ 4)) #(ответ 0)
print(int(5/ 4)) #(ответ 1)
#Если Преобразовать Float(Число с остатком) в Обычное число то оно округляется в меньшую сторону в любом случаи
print("Вот это команда Round")
print(round(0.4))  #(ответ 0)
print(round(0.5)) #(ответ 0)
print(round(0.51)) #(ответ 1)
print(round(0.7)) #(ответ 1)
#А так же есть команда `round()` которая округляет математически то есть
#0.51-0.999 округляется к 1 ,а вот 0.5-0.01 к 0