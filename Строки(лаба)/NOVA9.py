# Тюпов Артем ИУ7-12

text = ['ббаапп ббаапп ббаапп.',
          'ббаапп ббаапп!',
          'ббаапп ббаапп ббаапп ',
          'ббаапп ббаапп.']
          
ArrayOfSen=[]
ClauseEnd='.!?'
Sen=''
def Word(word):
    A=True
    for i in range(len(word)):
        k=0
        for j in range(i+1,len(word)-1):
            if word[i]==word[j]:
                k+=1
        if k==0:
            A=False
    return A

for i in range(len(text)):
    Str=text[i]
    for j in range(len(Str)):
        if Str[j] not in ClauseEnd:
            Sen+=Str[j]
        else:
            Sen+=Str[j]+' '
            ArrayOfSen.append(Sen)
            Sen=''
Max=0
s=''
IndexSen=0
##def SLOVO(char):
##    sl=''
##    if char != ' ':
##        Sl=char
##    return 
for i in range(len(ArrayOfSen)):
    Str=ArrayOfSen[i]
    Flag=True
    k=0
    for j in range(len(Str)):
        if Str[j]!=' ':
            s+=Str[j]
            print(s)
        else:
            if not Word(s):
                Flag=False
            else:
                Flag=True
                k+=1
    if k>Max:
        Max=k
        IndexSen=i
print('Предложение: ',ArrayOfSen[IndexSen])
print('Кол-во слов: ',Max)
