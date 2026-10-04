total = int(input("Введите количество порций: "))
capacity = int(input("Введите количество порций на подносе: "))
print('----------------------------')
if capacity < 0:
    print("Некорректный ввод данных")
else:
    full = total // capacity
    remainder = total % capacity
    units = (total + capacity - 1) // capacity
    print(f"Полных: {full}")
    print(f"Остаток: {remainder}")
    print(f"Всего: {units}")
print('----------------------------')