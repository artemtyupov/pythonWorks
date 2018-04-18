#Тюпов Артем.
#Написать и отладить программу находящую значения перменных x и y.
from math import log10,sin,pow

if __name__ == "__main__":
    #Вводятся аргументы a и b.
    try:
        a=input('Введите a: ')
        a=float(a)
        b=input('Введите b: ')
        b=float(b)
        x=input('Введите x: ')
        x=float(x)
        y=input('Введите y: ')
        y=float(y)
        if (y>=x):
            z = pow(a*a*a-8*b*y,1/3)
            print('z= {:5.3f}'.format(z))
        if (x>y) and (x>0) and (a>0):
            z = log10(x)-sin(2*y)
            print('z= {:5.3f}'.format(z))
        if (x>y) and (a<0): print('Переменная a не может быть меньше нуля!')
        if (x>y) and (x<0): print('Переменная x не может быть меньше нуля!')
        
    except ValueError:
        print('Пишите цифры')
    
    
        
    
        
