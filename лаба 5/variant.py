t = input("Введите текст: ")
g = "аеёиоуыэюя"
k = 0
for w in t.split():
    c = w.strip(".,!?;:").lower()
    if c == "":
        continue
    if c[0] in g:
        print(c)
        k += 1
if k == 0:
    print("Нет совпадений")
print(f"Количество: {k}")