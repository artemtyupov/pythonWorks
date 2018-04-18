#Тюпов Артем ИУ7-12

n1,n2=map(int,input('Введите количество столбцов и строк: ').split())
R=[]
a=[]
H=[]
k=0
z=[]
MT=[]
for i in range(n2):
    l=input('Введите строчку матрицы: ').split()
    m=map(int,l)
    a=list(m)
    R.append(a)
minR=R[0][0]
sa=[]
print('Введенная матрица: ')
for i in range(n1):
    print()
    for j in range(n2):
        print('{:5d}'.format(R[i][j]),' ',end='')

for i in range(n1):
    for j in range(n2):
        if R[i][j]<minR:
            minR=R[i][j]
            k=j
X=[]
for i in range(n1):
    X=[]
    for j in range(n2):
        if j==k:
           H.append(R[i][j]) 
        if j!=k:
           X.append(R[i][j])
    z.append(X)
print()
print('Вычеркнутый столбец: ')
for i in range(len(H)):
    print(H[i],' ',end='')
print()
print('Измененная матрица: ')
for i in range(len(z)):
    print()
    for j in range(len(z[i])):
        print('{:5d}'.format(z[i][j]),' ',end='')
print()
n1=len(z)
n2=len(z[1])
k=0
S=0
for i in range(n2):
    k=0
    S=0
    for j in range(n1):
        S+=z[j][i]
        k+=1
    sa1=S/k
    sa.append(sa1)
o=0
for i in range(n2):
    o=0
    for j in range(n1):
        if z[j][i]>sa[i]:
            o+=1
    MT.append(o)
print('Средние арифметические столбцов: ')
for i in range(len(sa)):
    print('{:.5f}'.format(sa[i]),' ',end='')
print()
print('Вектор MT: ')
for i in range(len(MT)):
    print(MT[i],' ',end='')
            
        
        

