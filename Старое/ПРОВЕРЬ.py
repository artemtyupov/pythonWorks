#Тюпов Артем ИУ7-12
#Сделать таблицу значений двух функций и построить одну из них
from math import sin,cos,floor
try:
    xmin,xmax=map(float,input('Диапазон через пробел: ').split(' '))
    hn=float(input('Шаг: '))
    k=1
    disY='-'*89+'> y'
    print('  x\t','    y1\t','      y2\t')
    p1max=p1min=sin(xmin)+0.6*cos(xmin)*xmin
    p2max=p2min=xmin**3-5.09*xmin**2+4.57*xmin+3.2
    i=xmin
    while i<(xmax+hn):
        p1=sin(i)+0.6*cos(i)*i
        p2=i**3-5.09*i**2+4.57*i+3.2
        if (p1>p1max):
            p1max=p1
        if (p1<p1min):
            p1min=p1
        print('{:.2f}'.format(i),'{:15.5f}'.format(p1),'{:15.5f}'.format(p2))
        i+=hn
    print(disY)
    j=xmin
    disX=5+(0-p1min)/(p1max-p1min)*59
    print('y=sint(t)+0.6*t*cos(t)')
    print(disX)
    while j<(xmax+hn):
        p1=sin(j)+0.6*cos(j)*j
        dis=5+(p1-p1min)/(p1max-p1min)*59
        if (dis<disX):
            print('{:15.5f}'.format(j),round(dis)*' ',
                  '*',round(disX-dis-1)*' ','|')  
        elif (dis>disX):
            print('{:15.5f}'.format(j),round(disX)*' ',
                  '|',round(dis-disX-1)*' ','*')
        else :
            print('{:15.5f}'.format(j),round(dis)*' ','*')  
        j+=hn

except ValueError:
    print('Вводите числа')
except ZeroDivisionError:
    print('Деление на ноль')


