c=0
sum=0
n=int(input())
for i in range(n):
    x=int(input())
    if abs(x)%10==2:
        c+=1
        sum+=x
print('Количество чисел, оканчивающихся на 2:', c)
print('Сумма чисел, оканчивающихся на 2:', sum)
