#Артем Тюпов ИУ7-12
#Даны 2 массива из целых чисел. Найти элементы, которых
#нет одновременно и в том, и в другом массиве
try:
    c=b=a=[]
    print(a)
    l1=input('Введите в 1 строку 1ый массив').split()
    m1=map(int,l1)
    a=list(m1)
    l2=input('Введите в 1 строку 2ой массив').split()
    m2=map(int,l2)
    b=list(m2)
    print()
    print('Первый массив: ')
    print(a)
    print('Второй массив: ')
    print(b)
    n1=len(a)
    n2=len(b)
    A=False
    k=0
    for i in range(n1):
        A=True
        for j in range(n2):
            if a[i]==b[j]:
                A=False
        if A==True:
            c.append(a[i])
    for i in range(n2):
        A=True
        for j in range(n1):
            if a[j]==b[i]:
                A=False
        if A==True:
            c.append(b[i])
    print('Элементы, которых нет одновременно ни в 1ом, ни во 2ом массиве: ')
    print(c)
except ValueError:
    print('Вводите все элементы через пробелы, только целые числа')
