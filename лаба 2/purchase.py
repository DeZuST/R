price=int(input("Введите цену одной тетради в целых рублях: "))
count=int(input("Введите количество тетрадей: "))
total_price=price*count
paid=int(input("Введите внесённую сумму: "))
print('-------------------------------------')
print(f"Общая стоимость: {total_price} руб.")
print('-------------------------------------')
if paid>=total_price:
    print(f"Сдача: {paid-total_price} руб.")
else:
    print("Недостаточно денег для покупки. Необходимо внести ещё: ", total_price-paid, "руб.")
print('-------------------------------------')