language = input("What language do you use?")

if language == "Python":
    print("Welcome to Python")
else:
    print("иди отсюда")

age = int(input("What is your age?"))

if age < 18:
    print("Уходи отсюда")
elif 18 <= age < 98:
    print("Проходите")
elif age >= 99:
    print("Вы старец или врун")
else:
    print("Вам либо много лет либо вы врун")