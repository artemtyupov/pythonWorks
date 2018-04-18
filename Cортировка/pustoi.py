#Тюпов Артем ИУ7-22

import numpy as np
import random as ran
from time import clock, sleep
a = np.array([ran.randint(-500, 500) for i in range(10000)])
b = np.array([a[i] for i in range(len(a))])
print('Исходный массив: ')
##for i in range(len(a)):
##    
##    print(a[i], end=' ')
##print()
print()
clock()
i = 2
for i in range(len(a)):
    if a[i-1] > a[i]:
        a[0] = a[i]
        j = i - 1
        while (j > 0) and (a[j] > a[0]):
            a[j+1] = a[j]
            j = j - 1
        a[j+1] = a[0]
t1 = clock()
for i in range(0,len(b)-1,1):
    for j in range(len(b)-2,i,-1):
        if b[j] > b[j+1]:
            b[j], b[j+1] = b[j+1], b[j]
t2 = clock() - t1
print('Метод вставки с барьером: ')
##for i in range(1,len(a)):
##    print(a[i], end=' ')
print()
print('Время исполнения сортировки этим методом: {:.5f} секунд'.format(t1))
print()
print('Метод улучшенного пузырька: ')
##for i in range(1,len(b)):
##    print(b[i], end=' ')
print()
print('Время исполнения сортировки этим методом: {:.5f} секунд'.format(t2))
