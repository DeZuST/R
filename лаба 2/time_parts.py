total_seconds=int(input("Введите количество секунд: "))
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60
if total_seconds<0:
    print('----------------------------')
    print("Некорректный ввод данных")
    print('----------------------------')
else:
    print(f"{hours} ч {minutes} м {seconds} с")