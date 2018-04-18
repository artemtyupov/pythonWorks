#Тюпов Артем.
#Найти сумму ряда с точностью E, без использования
#функции факториала.
try:
    x=int(input('Введите значение x: '))
    E=float(input('Введите значени точности E: '))
    curSum=1
    curItem=1
    k=1
    while abs(curItem)>E:
        prevSum=curSum
        prevItem=curItem
        f=k*(k+1)
        curItem=prevItem*(x**2/f)
        curSum+=curItem
        k+=2
    print('Значение суммы = {:.5f}'.format(curSum))    
except ValueError:
    print('Вводите числа')
except ZeroDivisionError:
    print('Деление на ноль')
