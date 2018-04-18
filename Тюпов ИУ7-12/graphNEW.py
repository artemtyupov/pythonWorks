from math import sin,cos,floor
try:
    xmin,xmax=map(int,input('Диапазон через пробел: ').split(' '))
    hn=int(input('Шаг: '))
    disX=59
    k=1
    disY='-'*119+'> y'
    print('  x\t','  y1\t','     y2\t')
    p1max=p1min=sin(xmin)+0.6*cos(xmin)*xmin
    p2max=p2min=xmin**3-5.09*xmin**2+4.57*xmin+3.2
    for i in range(xmin,xmax+1,hn):
        p1=sin(i)+0.6*cos(i)*i
        p2=i**3-5.09*i**2+4.57*i+3.2
        if (p1>p1max):
            p1max=p1
        if (p1<p1min):
            p1min=p1
        print('{:3d}'.format(i),'{:11.4f}'.format(p1),'{:11.4f}'.format(p2))
        k+=1
    print(disY)
    for j in range(xmin,xmax+1,hn):
        p1=sin(j)+0.6*cos(j)*j
        dis=1+(p1-p1min)/(p1max-p1min)*59
        if (dis<disX) and (dis!=1):
            print(str(j)+' '+floor(dis-len(str(j)))*' '+'*'+floor(disX-dis)*' '+'|')
        if (dis>disX) and (dis!=1):
            print(str(j)+' '+floor(disX-len(str(j)))*' '+'|'+floor(dis-disX)*' '+'*')
        if (dis<disX) and (dis==1):
            print(str(j)+' '+floor(dis-len(str(j)))*' '+'*'+floor(disX-dis-2)*' '+'|')
        if (dis>disX) and (dis==1):
            print(str(j)+' '+floor(disX-1-len(str(j)))*' '+'|'+floor(dis-disX)*' '+'*')
            
            
    print((disX)*' '+'\/ x')
except ValueError:
    print('Вводите числа')
except ZeroDivisionError:
    print('Деление на ноль')


