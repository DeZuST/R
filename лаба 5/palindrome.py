t = input("Введите текст: ")
c = t.lower().replace(" ", "")
if c == "":
    print("Нет текста")
elif c == c[::-1]:
    print("Палиндром")
else:
    print("Не палиндром")