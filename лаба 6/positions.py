t = input("Целые числа через пробел: ")
a = []
for p in t.split():
    a.append(int(p))
if len(a) == 0:
    print("Нет данных")
else:
    m = max(a)
    r = []
    for i, x in enumerate(a):
        if x == m:
            r.append(i)
    print(r)
