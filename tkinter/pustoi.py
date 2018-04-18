#Тюпов Артем

from tkinter import *

def proverka(p1,q1,p2,q2,x1,y1,x2,y2):
    
    Flag = False
    if (p2 - q1 != 0):
        if ((y1 > ((x1-p1)*(q2-q1)+q1*(p2-p1))/(p2-q1)) and (y2 <
((x2-p1)*(q2-q1)+q1*(p2-p1))/(p2-q1))) or ((y2 > ((x2-p1)*(q2-q1)+
q1*(p2-p1))/(p2-q1)) and (y1 <((x1-p1)*(q2-q1)+q1*(p2-p1))/(p2-q1))):
            Flag = True
    return Flag

array1 = []
array2 = []

array1.append('')
array2.append('')

i = 0
##print('Ввод множества А, по окончанию ввода, введите 0.')
##while array1[i] != '0':
##    array1.append(input('Введите координату: '))
##    i += 1
##    
##i = 0
##print('Ввод множества Б, по окончанию ввода, введите 0.')
##while array2[i] != '0':
##    array2.append(input('Введите координату: '))
##    i += 1
##
##array1.remove('')
##array1.remove('0')
##array2.remove('')
##array2.remove('0')
array1 = ['1 3','-5 -3','-7 8']
array2 = ['-5 2','-4 8','-1 4','2 1','4 5','7 -4']
maxnumber = 0
p_main1 = 0
q_main1 = 0
p_main2 = 0
p_main2 = 0
for i1 in range(len(array1)):
    p1,q1 = map(int,array1[i1].split())
    for i2 in range(len(array1)):
        if i1 != i2:
            p2,q2 = map(int,array1[i2].split())
            Flag = False
            numberoftreug = 0
            p = 1
            for j in range(len(array2)-1):
                p = j % 4
                x1,y1 = map(int,array2[j].split())
                x2,y2 = map(int,array2[j+1].split())
                if p == 3:
                    x1,y1 = map(int,array2[j].split())
                    x2,y2 = map(int,array2[j-2].split())
                    p == 1
                
                Flag = proverka(p1,q1,p2,q2,x1,y1,x2,y2)
                if (Flag == True) and (p%3 == 0):
                    numberoftreug += 1
                if p == 3:
                    p = 1
            if numberoftreug > maxnumber:
                maxnumber = numberoftreug
                p_main1 = p1
                q_main1 = q1
                p_main2 = p2
                q_main2 = q2
if maxnumber > 1:
    maxnumber -= 1
print('Количество треугольников: ', maxnumber)
print('Первая точка: (', p_main1,';', q_main1,')')
print('Вторая точка: (', p_main2,';', q_main2,')')

window = Tk()
window.title('Тюпов Артем ИУ7-22')
c1 = Canvas(window, width=1920, height=1080, cursor='pencil', bg='white')
c1.pack()
i = 0
for i in range(len(array1)):
    p1,q1 = map(int,array1[i].split())
    c1.create_oval(p1*50+600,q1*50+400,p1*50+600,q1*50+400,fill='red',outline='red', width=5)

c1.create_line(1540,0,0,955,width=2, fill='blue')
##
##yline1 = ((2025-p_main1)*(q_main2-q_main1)+q_main1*(p_main2-p_main1))/(p_main2-q_main1)
##xline1 = ((q_main1-1000)*(p_main2-p_main1)+p_main1*(q_main1-q_main2))/(q_main2-q_main1)
##yline2 = ((-24.75-p_main1)*(q_main2-q_main1)+q_main1*(p_main2-p_main1))/(p_main2-q_main1)
##xline2 = ((q_main1-0)*(p_main2-p_main1)+p_main1*(q_main1-q_main2))/(q_main2-q_main1)
##c1.create_line(xline1*50+600,yline1*50,xline2*50+600,yline2*50,width=2, fill='red')
##yline1 = ((1000-p_main1*50+600)*(q_main2*50+400-q_main1*50+400)+(q_main1*50+400)*(p_main2*50+600-p_main1*50+600))/(p_main2*50+600-q_main1*50+400)
##xline1 = ((q_main1*50+400-1000)*(p_main2*50+600-p_main1*50+600)+(p_main1*50+600)*(q_main1*50+400-q_main2*50+400))/(q_main2*50+400-q_main1*50+400)
##yline2 = ((0-p_main1*50+600)*(q_main2*50+400-q_main1*50+400)+(q_main1*50+400)*(p_main2*50+600-p_main1*50+600))/(p_main2*50+600-q_main1*50+400)
##xline2 = ((q_main1*50+400-0)*(p_main2*50+600-p_main1*50+600)+(p_main1*50+600)*(q_main1*50+400-q_main2*50+400))/(q_main2*50+400-q_main1*50+400)
##c1.create_line(xline1,yline1,xline2,yline2,width=2, fill='red')
for j in range(0,len(array2)-2,3):
    x1,y1 = map(int,array2[j].split())
    x2,y2 = map(int,array2[j+1].split())
    x3,y3 = map(int,array2[j+2].split())
    c1.create_line(x1*50+600,y1*50+400,x2*50+600,y2*50+400,width=2,fill='black')
    c1.create_line(x1*50+600,y1*50+400,x3*50+600,y3*50+400,width=2,fill='black')
    c1.create_line(x2*50+600,y2*50+400,x3*50+600,y3*50+400,width=2,fill='black')
                
window.mainloop()
                
        


    
