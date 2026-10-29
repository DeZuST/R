t = input("Целые числа через пробел: ")
a = []
for p in t.split():
    a.append(int(p))
b = []
for x in a:
    if x < 0:
        b.append(-x)
    else:
        b.append(x)
print(f"Исходный список: {a}")
print(f"Новый список: {b}")
