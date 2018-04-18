#Тюпов Артем.
s1=input('Введите текст: ')
s=s1+' '
x=[]
n=len(s)
while s!='':
    k=0
    while s[k]!=' ':
        k+=1
    x.append(s[:k])
    s=s[k+1:]
print('Слова, которые входят в текст 1 раз: ')
l=0
for i in range(len(x)):
    A=True
    for j in range (len(x)):
        if i!=j:
            if x[i]==x[j]:
                A=False
    if A==True:
        print(x[i],' ',end='')
        l+=1
if A==False and l==0:
    print('Таких слов нет')
         
    
    
    
        
    
        

