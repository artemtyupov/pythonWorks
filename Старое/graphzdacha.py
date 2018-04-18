#Тюпов Артем ИУ7-12
#Сделать таблицу значений двух функций и построить одну из них
#y1=sin(i)+0.6*cos(i)*i
#y2=i**3-5.09*i**2+4.57*i+3.2
from math import sin, cos
try:
    b, c, h = map(float,input('Введите начальное значение X, \
    конечное значение X, и значение шага счета значений функции: ').split())

    p1min = 1e30
    p1max = -1e30
    x = b
    n = round((c - b) / h)

    for i in range(n+1):
        p1=sin(i)+0.6*cos(i)*i
        p2=i**3-5.09*i**2+4.57*i+3.2
        if (p1>p1max):
                p1max=p1
        if (p1<p1min):
                p1min=p1
        print('{:.2f}'.format(i),'{:15.5f}'.format(p1),'{:15.5f}'.format(p2))
        x += h
    print()
    print('%.3f' % p1min, ' ' * 45, '%10.3f' % p1max, sep = '')
    print('+', '-' * 58, '+', '           X', sep = '')

    x = b

    for i in range(n+1):
        p1 = sin(i)+0.6*cos(i)*i
        disX = round((0 - p1min) / (p1max - p1min) * 59)
        dis = round((p1 - p1min) / (p1max - p1min) * 59)

        if p1min <= 0:
            if disX < dis:
                print(' ' * disX, '|', ' ' * (dis - disX - 1), '*', 
                      ' ' * (60 - dis - 1), sep = '', end = '')
                print('%15.3f' % x)
            elif dis < disX:
                print(' ' * dis, '*', ' ' * (disX - dis - 1), '|',
                      ' ' * (60 - disX - 1), sep = '', end = '')
                print('%15.3f' % x)
            else:
                print(' ' * dis, '*', ' ' * (60 - dis - 1), sep = '', end = '')
                print('%15.3f' % x)
        else:
            print(' ' * dis, '*', ' ' * (60 - dis - 1), sep = '', end = '')
            print('%15.3f' % x)
            
        x += h
except ValueError:
    print('Вводите числа')
except ZeroDivisionError:
    print('Деление на ноль')
