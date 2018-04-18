#Тюпов Артем ИУ7-22
def f(x):
    return x**2

def TrueValueI(a,b):
    ProizY1=a**3/3
    ProizY2=b**3/3
    return abs(ProizY1-ProizY2)

def integral(a, b, n):
    h = (a + b) / n
    fa = f(a)
    fb = f(b)
    x = a
    summ = 0
    x = x + h
    for i in range(2,n+1):
        y = f(x)
        x = x + h
        summ += y
        
    I = h * ((fa+fb) / 2 + summ)
    return I   
    
def function1():
    E = float(input('Введите точность E: '))
    i2n = E
    i1n = -1
    n1 = 0
    Iconst = TrueValueI(0, 3)
    while abs(i2n - i1n) > E:
        n1 += 2
        n2 = 2 * n1
        i1n = integral(0, 3, n1)
        i2n = integral(0, 3, n2)
    print('Количество шагов: ', n1)
    print(i2n)
##    print('Абсолютная ошибка: {:15.9f}'.format(abs(Iconst - i1n)))
##    print('Относительная ошибка: {:15.9f}'.format(abs((Iconst - i1n) / Iconst)))

def function2():
    a, b = map(float, input('Введите диапазон интегрирования: ').split())
    n = int(input('Введите количество разбиений: '))
    I = integral(a, b, n)
    print('Значение интеграла: ', I)
    
MenuElem = 4
while MenuElem != 0:
    print()
    print('Выход = 0')
    print('Интеграл с заданной точностью = 1')
    print('Интеграл с заданным диапазоном = 2')
    MenuElem = int(input('Для выбора пункта введите указанную цифру: '))

    if MenuElem == 0:
        exit
    elif MenuElem == 1:
        function1()
    elif MenuElem == 2:
        function2()

        
