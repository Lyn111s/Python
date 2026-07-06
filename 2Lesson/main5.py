score = 59

match score:
    case s if s >= 90:
        print("Оценка Отлично")
    case s if s >= 75:
        print("Оценка Хороша")
    case s if s >= 60:
        print("Оценка Пойдет")
    case _:
        print('Тест не сдан')
