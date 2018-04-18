#Тюпов Артем.
#Написать программу, которая определяет длины сторон треугольника по задан. коорд.
#Также тип треугольника, принадлежность точки треугольнику и длину.
#Вводятся координаты 3ех точек.
from math import sqrt,acos,cos,degrees
try:
    x1,y1=map(int,input('Введите x1,y1: ').split(' '))
    x2,y2=map(int,input('Введите x2,y3: ').split(' '))
    x3,y3=map(int,input('Введите x3,y3: ').split(' '))
    x,y=map(int,input('Введите x,y: ').split(' '))
    leng1=float(sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)))
    leng2=float(sqrt((x3-x2)*(x3-x2)+(y3-y2)*(y3-y2)))
    leng3=float(sqrt((x1-x3)*(x1-x3)+(y1-y3)*(y1-y3)))
    a1=degrees(acos((x1*x2+y1*y2)/(leng1*leng2)))
    a2=degrees(acos((x3*x2+y3*y2)/(leng3*leng2)))
    a3=degrees(acos((x1*x3+y3*y1)/(leng1*leng3)))
    if (a1>a2) and (a1>a3):
        biss=float(sqrt(leng2**2+leng3**2-2*leng2*leng3*cosa2))
    if (a2>a1) and (a2>a3):
        biss=float(sqrt(leng2**2+leng3**2-2*leng2*leng3*cosa2))
    if (a3>a2) and (a3>a1):
        biss=float(sqrt(leng2**2+leng3**2-2*leng2*leng3*cosa2))
    if (a3==a2) and (a2==a1):
        biss=float(sqrt(leng2**2+leng3**2))
    a1=y2-y1
    a2=y3-y2
    a3=y1-y3
    b1=x1-x2
    b2=x2-x3
    b3=x3-x1
    c1=x1*(y1-y2) + y1*(x2-x1)
    c2=x2*(y2-y3) + y2*(x3-x2)
    c3=x3*(y3-y1) + y3*(x1-x3)
    #1
    if (((x1<x2)and(y1<y2)) or ((x1>x2)and(y2<y1))) and (y3<((-a1*x3-c1)/b1)):
        if (y<=((-a1*x-c1)/b1))and(y>=((-a2*x-c2)/b2))and(y>=((-a3*x-c3)/b3)):
            print('Точка принадлежит заштрихованной области')
        else:
            print('Точка не принадлежит заштрихованной области')
    #2        
    if (((x1<x2)and(y1<y2)) or ((x1>x2)and(y2<y1))) and (y3>((-a1*x3-c1)/b1)):
        if (y>=((-a1*x-c1)/b1))and(y<=((-a2*x-c2)/b2))and(y<=((-a3*x-c3)/b3)):
            print('Точка принадлежит заштрихованной области')
        else:
            print('Точка не принадлежит заштрихованной области')        
    #3        
    if (((x2<x1)and(y1<y2)) or ((x1<x2)and(y2<y1))) and (y3>((-a1*x3-c1)/b1)):
        if (y>=((-a1*x-c1)/b1))and(y<=((-a2*x-c2)/b2))and(y<=((-a3*x-c3)/b3)):
            print('Точка принадлежит заштрихованной области')
        else:
            print('Точка не принадлежит заштрихованной области')
    #4        
    if (((x2<x1)and(y1<y2)) or ((x1<x2)and(y2<y1))) and (y3<((-a1*x3-c1)/b1)):
        if (y<=((-a1*x-c1)/b1))and(y>=((-a2*x-c2)/b2))and(y>=((-a3*x-c3)/b3)):
            print('Точка принадлежит заштрихованной области')
        else:
            print('Точка не принадлежит заштрихованной области')        

            
    
            
except ValueError:
    print('Пишите цифры')
