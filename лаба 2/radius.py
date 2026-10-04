import math
radius = float(input("Введите радиус: "))
length = 2 * math.pi * radius 
area = math.pi * radius ** 2 
print('----------------------------')
print(f"Длина окружности: {length:.2f}") 
print(f"Площадь круга: {area:.2f}")
print('----------------------------')