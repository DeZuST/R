print('-----------------------------------------------------')
print('До преобразований')
first = "2"
second = "3"
print(first + second)

age = input("Возраст: ")
print('TypeError: can only concatenate str (not "int") to str')

first = 4
second = 7
third = 10
average = first + second + third / 3
print(average)
print('-----------------------------------------------------')
print('Исправленый код')
first = "2"
second = "3"
print(int(first) + int(second))

age = int(input("Возраст: "))
print(age+1)

first = 4
second = 7
third = 10
average = (first + second + third) / 3
print(average)