n=int(input())
sum=0
k=0
ma=0
for i in range(n):
    x=int(input())
    sum+=x
    if x>0:
        k+=1
    if x>ma:
        ma=x
print('Сумма:', sum)
print('число положительных значений:', k)
print('Максимальное значение:', ma)
