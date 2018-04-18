#y=x*x-5x+6

a,b,hn=map(float,input('Введите диапазон и шаг').split())
n=round((b-a)/hn)
x=a
ymax=ymin=x*x-5*x+6
for i in range(n+1):
    y=x*x-5*x+6
    if y>ymax:
        ymax=y
    if y<ymin:
        ymin=y
    x+=hn
x=a
for i in range(n+1):
    y=x*x-5*x+6
    d1=round((y-ymin)/(ymax-ymin)*59)
    d0=round((0-ymin)/(ymax-ymin)*59)
    if ymin<0:
        if d0<d1:
            print(' '*d0,'|',' '*(d1-d0-1),'*', sep = '')
        if d0>d1:
            print(' '*d1,'*',' '*(d0-d1-1),'|', sep = '')
        if d0==d1:
            print(' '*d1,'*', sep = '')
    else:
        print(' '*d1,'*', sep = '')
    x+=hn
