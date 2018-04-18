# Иксарица Никита
from math import sin, cos
b, c, h = map(float,input('Введите начальное значение X, \
конечное, и шаг: ').split())

min = 1e30
max = -1e30
x = b
n = round((c - b) / h)

for i in range(n+1):
    q = x*x-5*x+6
    if q < min:
        min = q
    if q > max:
        max = q
    x += h

print('%.3f' % min, ' ' * 45, '%10.3f' % max, sep = '')
print('+', '-' * 58, '+', '       X', sep = '')

x = b

for i in range(n+1):
    q = x*x-5*x+6
    s_0 = round((0 - min) / (max - min) * 59)
    s_n = round((q - min) / (max - min) * 59)
    if min<=0:
        if s_0<s_n:
            print(' '*s_0,'|',' '*(s_n-s_0-1),'*', sep = '')
        if s_0>s_n:
            print(' '*s_n,'*',' '*(s_0-s_n- 1), '|', sep = '')
        if s_0==s_n:
             print(' '*s_n,'*', sep = '')
    else:
        print(' '*s_n,'*', sep = '')



        
##    if min <= 0:
##        if s_0 < s_n:
##            print(' ' * s_0, '|', ' ' * (s_n - s_0 - 1), '*', 
##                  ' ' * (60 - s_n - 1), sep = '', end = '')
##            print('%15.3f' % x)
##            print(s_0,s_n)
##        elif s_n < s_0:
##            print(' ' * s_n, '*', ' ' * (s_0 - s_n - 1), '|',
##                  ' ' * (60 - s_0 - 1), sep = '', end = '')
##            print('%15.3f' % x)
##            print(s_0,s_n)
##        else:
##            print(' ' * s_n, '*', ' ' * (60 - s_n - 1), sep = '', end = '')
##            print('%15.3f' % x)
##            print(s_0,s_n)
##    else:
##        print(' ' * s_n, '*', ' ' * (60 - s_n - 1), sep = '', end = '')
##        print('%15.3f' % x)
##        print(s_0,s_n)
        
    x += h
