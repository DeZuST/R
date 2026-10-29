t = input("Целые числа через пробел: ")
a = []
for p in t.split():
    a.append(int(p))
b = []
for x in a:
    if str(x).replace("-", "").endswith("2"):
        b.append(x)
print(f"Список: {b}")
print(f"Количество: {len(b)}")
print(f"Сумма: {sum(b)}")
print(f"Отсортированная копия: {sorted(b)}")
