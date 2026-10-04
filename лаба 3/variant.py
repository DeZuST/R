value = int(input("Введите значение от 0 до 100: "))
print('----------------------------')
if value < 0 or value > 100:
    print("Ошибка диапазона")
elif value <= 44:
    print("Есть место")
elif value <= 94:
    print("Архив растёт")
else:
    print("Почти заполнен")
print('----------------------------')