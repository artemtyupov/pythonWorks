#Артем Тюпов ИУ7-12
#Вычислить сумму ряда t с точностью до E.
#В матрице Z(15,10) определить элементы, большее значение суммы ряда.
#Заполнить эти элементы в массив X.
#Поменять местами в массиве Х 1ый элемент с максимальным.
#Напечатать сумму ряда, матрицу Z, вектор X.
try:
    from math import factorial
    a,E=map(float,input('Введите значние аргумента и\
 точность члена ряда: ').split())
    curItem = a**(-1)
    curSum = curItem
    k=2
    Z=[]
    X=[]
    l=0
    m=0
    y=0
    print('Член ряда: {:.5f}'.format(curItem))
    while abs(curItem) > E:
        prevItem = curItem
        prevSum = curSum
        curItem = prevItem*(a**2/(k*(k+1)))
        curSum = prevSum + curItem
        k = k + 2
        if y<5:
            print('Член ряда: {:.5f}'.format(curItem))
        y+=1
    print('Сумма ряда t с точностью E: {:.5f}'.format(curSum))

    n1,n2=map(int,input('Количество столбцов и строк: ').split())
    for i in range(n2):
        a=input('Введите строчку матрицы: ').split()
        m1=map(int,a)
        b=list(m1)
        Z.append(b)
        
    Xmax=curSum
    for i in range(n2):
        for j in range(n1):
            if Z[i][j] > curSum:
                X.append(Z[i][j])
    print('Сумма ряда t с точностью E: {:.5f}'.format(curSum))
    print('Начальный вектор X: ')
    for i in range(len(X)):
            print(X[i],' ',end='')
    print()
    for i in range(len(X)):
        if X[i]>Xmax:
            Xmax=X[i]
            l=i
                       
    X[0],X[l]=X[l],X[0]
    print('Измененный вектор X: ')
    for i in range(len(X)):
        print(X[i],' ',end='')
    print()
    print('Матрица: ')
    for i in range(n2):
        print()
        for j in range(n1):
            print('{:5.0f}'.format(Z[i][j]),' ', end='')
except ValueError:
    print('Неправильный ввод')
except ZeroDivisionError:
    print('Деление на ноль')
