#Тюпов Артем
from math import sin
def f(x):
    return sin(x)
try:
    a, b = map(float, input('Введите левый и правый конец отрезка: ').split())
    E = float(input('Введите точность аргумента: '))
    h = float(input('Введите значение шага: '))
    x = a
    while x <= b:
        Flag = False
        x1 = x
        x2 = x1 - ((f(x1)**2)/(f(x1+f(x1))-f(x1)))
        while (abs(x1-x2) > E) and (((f(x)<0) and (f(x+h)>0))
    or ((f(x)>0) and (f(x+h)<0))):
            Flag = True
            x1 = x2 - ((f(x2)**2)/(f(x2+f(x2))-f(x2)))
            x2 = x1 - ((f(x1)**2)/(f(x1+f(x1))-f(x1)))
        if Flag == True:
            print('xi = {:.7e}'.format(x1)+'  ' + 'xi+1 = {:.7e}   '.format(x2) +
              ' x = {:.3f}'.format(x))   
        x += h
except ValueError:
    print('Вводите числа')
except ZeroDivisionError:
    print('Деление на ноль')  
