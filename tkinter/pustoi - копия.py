##Тюпов Артем

from tkinter import *

array1=['']
array2=['']
i = 0
print('Ввод множества А, по окончанию ввода, введите 0.')
while array1[i] != '0':
    array1.append(input('Введите координату центра окружности и ее радиус: '))
    i += 1
i = 0

array1.remove('')
array1.remove('0')
array2 = array1
maxnumber = 0

for i in range(len(array1)):
    x1,y1,r1 = map(int,array1[i].split())
    flag1 = False
    flag2 = False
    number = 0
    for j in range(len(array2)):
        if i != j:
            x2,y2,r2 = map(int,array1[j].split())
            if ((x2-r2)<=r2) and ((x2+r2)<=r2) and ((y2-r2)<=r2) and ((y2+r2)<=r2):
                flag1 = True
            if (x2>=x1+r1) and (x2>=x1-r1) and (y2>=y1+r1) and (y2>=y1-r1):
                flag2 = True
            print(x1,y1,r1,x2,y2,r2)
##            if (x1==x2) and (y1==y2) and (r1>r2):
##                flag1 = True
##            if (x1 > x2) and (y1 > y2) and (r1>r2) and (x2<x1+r1) and (x2<x1-r1) and (y2<y1+r1) and (y2<y1-r1):
##                flag2 = True
##            if (x1 < x2) and (y1 < y2) and (r1>r2) and (x2<x1+r1) and (x2<x1-r1) and (y2<y1+r1) and (y2<y1-r1):
##                flag2 = True
##            if (x1 > x2) and (y1 < y2) and (r1>r2) and (x2<x1+r1) and (x2<x1-r1) and (y2<y1+r1) and (y2<y1-r1):
##                flag2 = True
##            if (x1 < x2) and (y1 > y2) and (r1>r2) and (x2<x1+r1) and (x2<x1-r1) and (y2<y1+r1) and (y2<y1-r1):
##                flag2 = True
            print(flag1,flag2)
            if flag1 or flag2:
                number += 1
    if number > maxnumber:
        maxnumber = number
        xmain = x2
        ymain = y2
        rmain = r2
        print(number,xmain,ymain,rmain)


window = Tk()
window.title('Тюпов Артем ИУ7-22')
c1 = Canvas(window, width=1920, height=1080, cursor='pencil', bg='white')
c1.pack()
i = 0
for i in range(len(array1)):
    x,y,r = map(int,array1[i].split())
    print('DDD',x,y,r)
    print('AAA',xmain,ymain,rmain)
    if (x == xmain) and (y == ymain) and (r == rmain):
        x1 = xmain-r
        x2 = xmain+r
        y1 = ymain-r
        y2 = ymain+r
        c1.create_oval(x1*50+400,y1*50+400,x2*50+400,y2*50+400,outline='green', width=5)
    else:
        x1 = x-r
        x2 = x+r
        y1 = y-r
        y2 = y+r
        c1.create_oval(x1*50+400,y1*50+400,x2*50+400,y2*50+400,outline='red', width=3)
                
window.mainloop()

