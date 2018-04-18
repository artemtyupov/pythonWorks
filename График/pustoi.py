#Тюпов Артем ИУ7-22

import matplotlib.pyplot as plt
import numpy as np
from math import *
def f(x):
    return cos(x*sin(x))
def pf(x):
    return -(x*cos(x)+sin(x))*sin(x*sin(x))
def p2f(x):
    return (x*sin(x)-2*cos(x))*sin(x*sin(x))+(-1*x*cos(x)-sin(x))*(x*cos(x)+sin(x))*cos(x*sin(x))
a, b = map(int,input('Введите границе графика по аргументу: ').split())
h = abs(b-a)/1000
x = np.linspace(a,b,1000)
y = np.cos(x*np.sin(x))
plt.plot(x,y,label='sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph')
Flag = False
Flag1 = False
Flag2 = False
Flag3 = False
i = a
max_f = f(a)
max_x = a
min_f = f(a)
min_x = a
i2 = a + h
flagone = False
flagtwo = False
if f(i2) > f(i):
    flagone = True
if f(i2) < f(i):
    flagtwo = True
l = 0
while i<b:
    i2 = i + h
    #Ищем максимум и минимум
    if f(i) > max_f:
        max_f = f(i)
        max_x = i
    if f(i) < min_f:
        min_f = f(i)
        min_x = i
    #Выделяем экстремумы
    if flagone == True:
        if f(i2) < f(i):
            marker2 = plt.scatter(i, f(i),s = 300, c = 'w', marker = (5,0))
            flagone = False
            flagtwo = True
    if flagtwo == True:
        if f(i2) > f(i):
            marker2 = plt.scatter(i, f(i),s = 200, c = 'w', marker = (5,0))
            flagone = True
            flagtwo = False
    #Выделяем точки перегиба
    if (p2f(i) >= -h/2) and (p2f(i) <= h/2):
        marker5 = plt.scatter(i, f(i), s = 200, c = 'w')
    #Выделяем нули функции    
    if (round(f(i))== 0) and (Flag == False):
        Flag = True
        l += 1
        if l != 1 :
            marker1 = plt.scatter(i, 0, s = 80, c = 'g')
        if f(i)>0:
            Flag1 = True
        if f(i)<0:
            Flag2 = True
        if f(i)==0:
            Flag3 = True
            
    if ((Flag1 == True) and (f(i)<0)) or (Flag3 == True):
        Flag1 = False
        Flag3 = False
        Flag = False
        
    if ((Flag2 == True) and (f(i)>0)) or (Flag3 == True):
        Flag2 = False
        Flag3 = False
        Flag = False
        
    i += h
marker3 = plt.scatter(max_x, max_f, s = 80, c = 'r')
marker4 = plt.scatter(min_x, min_f, s = 80, c = 'r')
plt.grid(True)
plt.axis('equal')
plt.legend([marker1, marker2, marker3, marker4, marker5],
           ['Nulls', 'Exstrmums', 'Max', 'Min', 'Peregib'])
plt.show()
