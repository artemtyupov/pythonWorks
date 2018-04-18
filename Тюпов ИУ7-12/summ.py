from math import factorial
try:
    x = int(input('Введите значение x: '))
    E = float(input('Введите точность E: '))
    n = int(input('Введите начальное значение N: '))
    hn = int(input('Введите значение шага hn: '))
    mx = int(input('Введите значение max: '))
    k1 = 1
    f = 1
    k2 = 2
    curSum = x
    curItem = x
    A=True
    print('Текущий номер элемента Текущий элемент  Текущая сумма\t',)
    while abs(curItem) > E:
        if k1 == mx:
            print('Значение суммы не сходиться')
            A=False
            break
        if A:
            prevItem = curItem
            prevSum = curSum
            
            if k1 >= n:
                #print('Текущий номер элемента, элемент и сумма \t')
                print(k1,"\t                {:.5f}".format(curItem),
                "\t  {:.5f}".format(curSum))
                
                n *= hn
            f*=(k2+1)*k2
            #curItem *= x**2/f
            curSum += curItem
            #k2 += 2
            k1 += 1
    if A:        
        print('При x = ',x,'с точностью = ',E,'сумма = {:.5f}'
        .format(curSum),'и число эл-ов = ',(k1-1))    
except ValueError:
    print('Вводите числа')
except ZeroDivisionError:
    print('Деление на ноль')
    

    
