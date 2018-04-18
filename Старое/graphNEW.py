#Тюпов Артем ИУ7-12
#Сделать таблицу значений двух функций и построить одну из них
from math import sin,cos,floor
try:
    xmin,xmax=map(float,input('Диапазон через пробел: ').split(' '))
    hn=float(input('Шаг: '))
    disX=59
    k=1
    disY='-'*89+'> y'
    print('  x\t','    y1\t','      y2\t')
    p1max=p1min=sin(xmin)+0.6*cos(xmin)*xmin
    p2max=p2min=xmin**3-5.09*xmin**2+4.57*xmin+3.2
    i=xmin
    while i<(xmax+1):
        p1=sin(i)+0.6*cos(i)*i
        p2=i**3-5.09*i**2+4.57*i+3.2
        if (p1>p1max):
            p1max=p1
        if (p1<p1min):
            p1min=p1
        print('{:.3f}'.format(i),'{:10.5f}'.format(p1),'{:10.5f}'.format(p2))
        i+=hn
    print(disY)
    #for j in range(xmin,xmax+1,hn):
    j=xmin
    print('y=sint(t)+0.6*t*cos(t)')
    while j<(xmax+1):
        p1=sin(j)+0.6*cos(j)*j
        dis=(p1-p1min)/(p1max-p1min)*59
        if (dis<disX):
            print('{:10.5f}'.format(j)+' '+int( round( dis ) )*' '+
                  '*'+int( round( disX-dis ))*' '+'|')
               
        if (dis>disX):
            print('{:10.5f}'.format(j)+' '+int( round( disX )  +1)*' '+
                  '|'+int( round( dis-disX) )*' '+'*')

        if (dis==disX):
            print('{:10.5f}'.format(j)+' '+int( round( dis ) )*' '+' *')

        j+=hn

            
            
    print((disX+12)*' '+'\/ x')
except ValueError:
    print('Вводите числа')
except ZeroDivisionError:
    print('Деление на ноль')


