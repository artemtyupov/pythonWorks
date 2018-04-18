from math import sqrt,degrees,cos
try:
    x1,y1=map(int,input('Введите координаты 1ой: ').split(' '))
    x2,y2=map(int,input('Введите координаты 2ой: ').split(' '))
    x3,y3=map(int,input('Введите координаты 3ой: ').split(' '))
    x4,y4=map(int,input('Введите координаты точки: ').split(' '))
    l1=sqrt((x4-x1)**2+(y4-y1)**2)
    l2=sqrt((x4-x2)**2+(y4-y2)**2)
    l3=sqrt((x4-x3)**2+(y4-y3)**2)
    leng1=sqrt((x2-x1)**2+(y2-y1)**2)
    leng2=sqrt((x3-x2)**2+(y3-y2)**2)
    leng3=sqrt((x1-x3)**2+(y1-y3)**2)
    p1=(leng1+l1+l2)/2
    p2=(leng2+l3+l2)/2
    p3=(leng3+l1+l3)/2
    s1=sqrt(p1*(p1-l1)*(p1-l2)*(p1-leng1))
    s2=sqrt(p2*(p2-l3)*(p2-l2)*(p2-leng2))
    s3=sqrt(p3*(p3-l1)*(p3-l3)*(p3-leng3))
    h1=2*s1/leng1
    h2=2*s2/leng2
    h3=2*s3/leng3
    if (h1>h2)and(h1>h3): print('Расстояние = ',h1)
    if (h2>h3)and(h2>h1): print('Расстояние = ',h2)
    if (h3>h2)and(h3>h1): print('Расстояние = ',h3)
except ValueError:
    print('Пишите числа через пробел')
except ZeroDivisionError:
    print('Деление на ноль')
