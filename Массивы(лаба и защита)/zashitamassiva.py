#Тюпов Артем ИУ7-12
n=input('Введите число: ')
a=[]
N=len(n)
for i in range(N):
    b=''
    b=n[:1]
    if b!='-':
        a.append(b)
    c=n[1:]
    n=''
    n=c
print('Полученный массив: ')
for i in range(len(a)):
    print(a[i],' ',end='')
