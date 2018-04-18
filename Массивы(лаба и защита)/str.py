#Артем Тюпов
#В строке указано число N и N целых чисел (2<=N<=37).
#Определить упорядочены ли элементы по неубыванию или
#по невозрастанию. Массивов не использоват.
try:
    s=input()
    A=B=True
    s1=s2=s3=s4=''
    s1=s[1:]
    s1=s1[1:]
    s2=s[:1]
    print('Исходная строка: ',s1)
    print('Количество целых чисел исходной строки: ',s2)
    i=0
    s1+=' '*3
    N=len(s1)-3
    while i<=(N-1):
        s3=''
        while s1[i]!=' ':
            s3+=s1[i]
            i+=1
        i+=1
        if s3!='' and s4!='':
            if int(s4)<int(s3): A=False
            if int(s4)>int(s3): B=False
        s4=''
        while s1[i]!=' ':
            s4+=s1[i]
            i+=1
        if s3!='' and s4!='':
            if int(s3)<int(s4): A=False
            if int(s3)>int(s4): B=False
        i+=1
    if (A==True):
        print('Числа упорядочены по невозрастанию')
    if (B==True):
        print('Числа упорядочены по неубыванию')
    if (A==False) and (B==False):
        print('Числа не упорядочены')
except ValueError:
    print('Вводите данные в виде: 1 2 3 4 5')
