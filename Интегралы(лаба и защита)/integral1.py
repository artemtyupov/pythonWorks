#Тюпов Артем ИУ7-12
#Метод Монте-Карло и метод Уэддля
import random as random_number

S=0

#Функция    
def function(x):
    return x**2

#Истинное значение интеграла
def TrueValueI(a,b):
    ProizY1=a**3/3
    ProizY2=b**3/3
    return abs(ProizY1-ProizY2)

#Метод Монте-Карло
def MonteKarlo(a,b,n):
    S=0
    for i in range(n):
        x=random_number.uniform(a,b)
        S+=function(x)
    I=float((b-a)/n)*S
    return I
# Формула Уэддля:
def Ueddle(a,b,N):
    if (N%6==0):
        s=0
        curX=a
        prevX=a
        h=(b-a)/N
        n = N//6
        step = h
        L = [function(a)]*7
        I2 = 0

        for i in range(n):
            L[0] = L[6]
            for j in range(1,7):
                L[j] = function(a+step*(6*i+j))
            I2 += L[0] + 5*L[1] + L[2] + 6*L[3] + L[4] + 5*L[5] + L[6]
        
        I = float( I2*3*step/10 )
        return I
    else:
        return 100
#Главная часть
a,b=map(float,input('Введите диапазон интегрирования: ').split())
n1,n2=map(int,input('Введите количество разбиений для Монте-Карло: ').split())
n3,n4=map(int,input('Введите количество разбиений для Уэддля: ').split())
Imonte1=MonteKarlo(a,b,n1)
Imonte2=MonteKarlo(a,b,n2)
Iueddle1=Ueddle(a,b,n3)
Iueddle2=Ueddle(a,b,n4)
Iconst=TrueValueI(a,b)


#Вывод    
print('Метод',' '*9,'n1 = {:3.0f}'.format(n1),
' '*7,'n2 = {:3.0f}'.format(n2),)
print('Монте-Карло','{:15.9f}'.format(Imonte1),'{:15.9f}'.format(Imonte2))
print('Метод',' '*9,'n3 = {:3.0f}'.format(n3),
' '*7,'n4 = {:3.0f}'.format(n4),)
if Iueddle1==100 and Iueddle2!=100:
    print('Уэддля',8*' ','Не считается','{:14.9f}'.format(Iueddle2))
elif Iueddle1!=100 and Iueddle2==100:
    print('Уэддля',4*' ','{:15.9f}'.format(Iueddle1),3*' ','Не считается')
elif Iueddle1==100 and Iueddle2==100:
    print('Уэддля',8*' ','Не считается',2*' ','Не считается')
else:
    print('Уэддля',' '*4,'{:15.9f}'.format(Iueddle1),'{:15.9f}'.format(Iueddle2))
    
if abs(Iconst-Imonte1)<=abs(Iconst-Imonte2):
    Iabs1=Imonte1
else:
    Iabs1=Imonte2
if abs(Iconst-Iueddle1)<=abs(Iconst-Iueddle2):
    Iabs2=Iueddle1
else:
    Iabs2=Iueddle2
if abs(Iabs1-Iconst)<=abs(Iabs2-Iconst):
    Iabs=Iconst-Iabs1
##    print('Абсолютная ошибка: {:15.9f}'.format(Iabs))
else:
    Iabs=Iconst-Iabs2
##    print('Абсолютная ошибка: {:15.9f}'.format(Iabs))
Iotn=abs(Iabs/Iconst)
##print('Относительная ошибка: {:15.9f}'.format(Iotn))
#Вычисление с точностью E
E=float(input('Введите точность E: '))
i2n=E
i1n=-1
n1=10
if Iabs1-Iabs2<=0:
    n1=0
    while abs(i2n-i1n)>E:
        n1+=2
        n2=2*n1
        i1n=MonteKarlo(a,b,n1)
        i2n=MonteKarlo(a,b,n2)
    print('Количество шагов: ',n1,i1n)
    print('Абсолютная ошибка: {:15.9f}'.format(abs(Iconst-i1n)))
    print('Относительная ошибка: {:15.9f}'.format(abs((Iconst-i1n)/Iconst)))
    
else:
    n1=0
    
    while abs(i2n-i1n)>E:
        n1+=2
        n2=2*n1
        i1n=Ueddle(a,b,n1)
        i2n=Ueddle(a,b,n2)
    print('Количество шагов: ',n1, i1n)
    print('Абсолютная ошибка: {:15.9f}'.format(abs(Iconst-i1n)))
    print('Относительная ошибка: {:15.9f}'.format(abs((Iconst-i1n)/Iconst)))


