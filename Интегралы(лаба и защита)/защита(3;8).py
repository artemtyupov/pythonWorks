#Тюпов Артем.
a,b=map(int,input('Введите диапазон интегрирования: ').split())
n=int(input('Введите количество разбиений: '))

def f(y):
    return y**2
def Integral(a,b):
    Iconst1=b**3/3
    Iconst2=a**3/3
    return abs(Iconst2-Iconst1)
print('Фукнция y=x^2')
I=0
if n%3==0:
    h=(b-a)/n
    y=a
    for j in range(n):
        i=j+1
        y+=h
        yvalue=f(y)
        if i%3==0 and i!=n:
            I+=2*yvalue
        if i%3!=0:
            I+=3*yvalue
        if i==n:
            I+=yvalue
    I+=f(a)
    I*=3*h/8
    Iconst=Integral(a,b)
    print('Истинное значение интеграла: {:15.9f}'.format(Iconst))
    print('Высчитанное значение интеграла: {:15.9f}'.format(I))
else:
    print('Не считается, т.к. кол-во разбиений не кратно 3.')
    
    
        
    
        
