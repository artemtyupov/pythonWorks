#Артем Тюпов
#Сформировать вектор А из ненулевых элементов целочисленной матрицы R(9,7)
#В векторе А 4ый отрицательный элемент заменить произведением остальных
#Если в векторе АБ4 отрицательных элементов вывести соответствующий текст
#Напечатать матрицу R и вектор A

from random import randint
n1=int(input('Количество столбцов: '))
n2=int(input('Количество строк: '))
X=[]
z=[]
b=[]
r=k=0
p=1
R=[]
for i in range(n2):
    a=input('Введите строчку матрицы: ').split()
    m1=map(int,a)
    b=list(m1)
    R.append(b)
for j in range(n2):
    for i in range(n1):
        if R[i][j]!=0:
            X.append(R[i][j])
Xmax=X[0]
print('Начальный вектор A: ')
for i in range(len(X)):
        print(X[i],' ',end='')
print()
for i in range(len(X)):
    if X[i]<0:
        k+=1
        if k==4:
            r=X[i]
            s=i
            k+=1
    if k !=4:
        p*=X[i]
    if X[i]>Xmax:
        Xmax=X[i]
if r != 0:
    z=[]
    for i in range(len(X)):
        
        if (i!=s):
            z.append(X[i])
        else:
            z.append(p)
    print('Измененный вектор A: ')
    for i in range(len(z)):
        print(z[i],' ',end='')
else:
    print('Нет 4ого отрицательного')
print()
print('Матрица: ')
for i in range(n2):
    print()
    for j in range(n1):
        print('{:5.0f}'.format(R[i][j]),' ', end='')
