#Тюпов Артем ИУ7-22
from time import clock
from math import sin,tan,cos,log
###Значение функции
##def fx(x):
##    return exp(-x) - x
##
###Значение производной
##def proiz(x):
##    return -1-exp(-x)
##
###Выражение x
##def fxx(x):
##    #x=x-l*(f(x))
##    #l=1/max(f'(x))
##    return x-(1/proiz(x))*(exp(-x)-x)

###Значение функции
##def fx(x):
##    return tan(x)-x
##
###Значение производной
##def proiz(x):
##    return tan(x)*tan(x)
##
###Выражение x
##def fxx(x):
##    #x=x-l*(f(x))
##    #l=1/max(f'(x))
##    return x-(1/proiz(x))*(tan(x)-x)

#Значение функции
def fx(x):
    return cos(x)-x

#Значение производной
def proiz(x):
    return -sin(x)-1

#Выражение x
def fxx(x):
    #x=x-l*(f(x))
    #l=1/max(f'(x))
    return cos(x)




try:
    a, b = map(float, input('Введите левый и правый конец отрезка: ').split())
    E1 = float(input('Введите точность аргумента: '))
##    E2 = float(input('Введите точность функции: '))
    h = float(input('Введите значение шага: '))
    maxk = int(input('Введите максимальное количество итераций: '))
    x = a
    ErrorCode = 0
    n = 1
    clock()
    print('  №'+' '*3+'xn'+'   '+'xn+1'+' '*5+'x'+5*' '+'  f(x)'+' '*5
    +'Реальное количество итераций'+7*' '+'Код ошибки')
    while x <= b:
        ErrorCode = 0
        x1 = fxx(x)
        x2 = fxx(x1)
        print('Промежуточное значение итерации: {:10.7f}'.format(x2))
        k = 2
        while (abs(x2-x1) > E1) and (k < maxk) and (((fx(x)<0) and (fx(x+h)>0))
    or ((fx(x)>0) and (fx(x+h)<0))):
            k += 2
            x1 = fxx(x2)
            x2 = fxx(x1)
            print('Промежуточное значение итерации: {:10.7f}'.format(x1))
            print('Промежуточное значение итерации: {:10.7f}'.format(x2))
            
        if (k >= maxk):
            ErrorCode = 1
               
        if ((fx(x)<0) and (fx(x+h)<0)) or ((fx(x)>0) and (fx(x+h)>0)):
            ErrorCode = 2    
        if ErrorCode == 0 or ErrorCode == 1:
            n += 1
            print("{:3.0f}".format(n)+" {:5.1f}".format(x)+" {:5.2f}".format(x+h)
            +" {:10.7f}".format(x2)+' '+" {:7.3e}".format(fx(x2))+7*' '+'  '
            "  {:3.0f}".format(k)+25*' '+" {:3.0f}".format(ErrorCode))
##        if ErrorCode == 2:
##            print("{:3.0f}".format(n)+" {:5.1f}".format(x)+" {:5.2f}".format(x+h)
##            +5*' '+"-"+9*' '+"-"+9*' '+7*' '+" {:3.0f}".format(k)
##            +25*' '+" {:3.0f}".format(ErrorCode))
            
        
        x += h
    print()
    print('Время работы программы: {:10.5f}'.format(clock()))
    print()
    print('Код ошибки 0  - нет ошибки')
    print('Код ошибки 1 - первышено максимальное количество итераций')
    print('Код ошибки 2 - 0 или больше 1 корня на данном промежутке')
except ValueError:
    print('Вводите числа')
except ZeroDivisionError:
    print('Деление на ноль')
