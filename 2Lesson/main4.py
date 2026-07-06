is_sunny = False
is_weekend = True

if is_sunny and is_weekend:
    print("Идеальный день для прогулки")
elif is_sunny and not is_weekend:
    print("Погода хороша,но нужно поработать")
elif not is_sunny and is_weekend:
    print("Можно остаться дома и отдохнуть")
elif not is_sunny and not is_weekend:
    print('Рабочий день с плохой погодой')