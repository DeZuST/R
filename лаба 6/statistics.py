t = input("Целые числа через пробел: ")
n = []
for p in t.split():
    n.append(int(p))
if len(n) == 0:
    print("Нет данных")
else:
    print(f"Количество: {len(n)}")
    print(f"Сумма: {sum(n)}")
    print(f"Минимум: {min(n)}")
    print(f"Максимум: {max(n)}")
    print(f"Среднее: {sum(n) / len(n):.2f}")
