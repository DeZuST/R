from functions import average, normalize_text, select_numbers, sum_digits


def main():
    k = int(input("Целое число: "))
    print(f"Сумма цифр: {sum_digits(k)}")

    t = input("Целые числа через пробел: ")
    a = []
    for p in t.split():
        a.append(int(p))

    m = average(a)
    if m is None:
        print("Среднее: Нет данных")
    else:
        print(f"Среднее: {m:.2f}")

    print(f"Нормализованный текст: {normalize_text(input('Текст: '))}")

    g = int(input("Порог: "))
    print(f"Выборка: {select_numbers(a, g)}")


if __name__ == "__main__":
    main()
