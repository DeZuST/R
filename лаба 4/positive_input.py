t=0
c=0
while t==0:
    x=int(input())
    if x<=0:
        c+=1
    else:
        t=x**2
print('Квадрат числа:', t)
print('Количество отклонений:', c)