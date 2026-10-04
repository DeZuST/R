a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
operation = input("Введите операцию(+, -, *, /): ")
if operation not in ["+", "-", "*", "/"]:
    print('----------------------------')
    print("Неизвестная операция")
    print('----------------------------')
else:
    print('----------------------------')
    if operation == "+":
        result = a + b
        print(f"{result:.2f}")
    elif operation == "-":
        result = a - b
        print(f"{result:.2f}")
    elif operation == "*":
        result = a * b
        print(f"{result:.2f}")
    elif operation == "/":
        if b == 0:
            print("Деление на ноль запрещено")
        else:
            result = a / b
            print(f"{result:.2f}")
    else:
        print("Неизвестная операция")
    print('----------------------------')