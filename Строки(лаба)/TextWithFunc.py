# Тюпов Артем ИУ7-12
# Версия программы с использованием функций

text_1 = ['ПОВТОР Python 2+2 поддерживает несколько парадигм программирования',
          'в том числе структурное, объектно-ориентированное, функциональное,',
          'императивное, выгодное и аспектно-ориентированное.',
          'ПОВТОР Основные архитектурные черты - динамическая типизация,',
          'автоматическое управление памятью, полная интроспекция, механизм обработки',
          'исключений,поддержка многопоточных вычислений и удобные высокоуровневые',
          'структуры данных. 2*2 ПОВТОР Код в Python организовывается в функции и классы,',
          'которые могут объединяться в модули они в свою очередь могут быть',
          'объединены в различные многофункциональные пакеты 0*4']

# Функция выравнивания текста по правому краю
def reform_right(text):
    len_max_string = 0
    for string in text:
        if len(string) > len_max_string:
            len_max_string = len(string)
    for string in text:
        print('\t' + ' '*(len_max_string-len(string)) + string)

# Функция выравнивания по ширине
def format_width(string, n):
    a = string.split()
    l = 0
    for x in a:
        l+= len(x)
    if len(a) > 1:
        spaces = int((n-l)/(len(a)-1))
        extra = n-l-spaces*(len(a)-1)-1
        result = a[0] + ' '*(spaces+1)
        for i in range(1,len(a)-1):
            if extra > 0:
                result += a[i]
                for x in range(spaces+1):
                    result += ' '
                extra-=1
            else:
                result+= a[i] + ' '*spaces
        return result + a[len(a)-1]
    else:
        spaces = int((n-l)/2)
        extra = (n-l) % 2
        return ' '*(spaces+extra) + a[0] + ' '*(spaces)

clause_end = '.?!'
clause_cont = ',;:—'

# Форматируем количество пробеллов между словами и запоминаем кол-во
# в каждой строке
text_2 = []
string_count_word = []
for string in text_1:
    k = 0
    s = ''
    string = ' ' + string + ' '
    for i in range(1,len(string)):
        if string[i] != ' ':
            s += string[i]
        elif string[i-1] != ' ':
            s += ' '
            k += 1
    string_count_word.append(k)
    text_2.append(s)
    
# Замена арифметического выражения (+*) на результат
number = '0123456789'
for j in range(len(text_2)):
    s = text_2[j]
    i = 1
    while i < len(s)-1:
        if s[i] == '*' and s[i-1] in number and s[i+1] in number:
            k1 = k2 = ''
            t = i - 1
            q = i + 1
            while s[t] in number:
                k1 += s[t]
                t -= 1
            k1 = k1[::-1]
            while s[q] in number:
                k2 += s[q]
                q += 1
            s = s[:t+1] + str(int(k1)*int(k2)) + s[q:]
            
        if s[i] == '+' and s[i-1] in number and s[i+1] in number:
            k1 = k2 = ''
            t = i - 1
            q = i + 1
            while s[t] in number:
                k1 += s[t]
                t -= 1
            k1 = k1[::-1]
            while s[q] in number:
                k2 += s[q]
                q += 1
            s = s[:t+1] + str(int(k1)+int(k2)) + s[q:]
        text_2[j] = s
        i += 1

# Выравнивание строк по правому краю
print('\nВыравнивание по правому краю:\n')
reform_right(text_2)

# Выравнивание строк по ширине
print('\nВыравнивание по ширине:\n')
n = 0
for x in text_2:
    print(format_width(x, 78))
    if n < len(x):
        n = len(x)

# Переписываю весь текст в одну строку
s = ''
for string in text_2:
    s += string

# Поиск самых коротких и самых длинных слов в каждом предложении
word = ''
word_min_len = []
word_min_char = 0
word_max_char = 0
word_max_len=[]
for i in range(len(s)):
    if (s[i]!=' ') and (s[i] not in clause_end) and (s[i] not in clause_cont):
        word += s[i]
    if (s[i] == ' ' or s[i] in clause_end) and word != '':
        if len(word) < word_min_char or word_min_char == 0:
            word_min_char = len(word)
            word_min = word
        if len(word) > word_max_char or word_max_char == 0:
            word_max_char = len(word)
            word_max = word
        word = ''
    if s[i] in clause_end:
        word_min_len.append(word_min)
        word_min_char = 0
        word_max_len.append(word_max)
        word_max_char = 0
        word = ''
        word_min = ''
        word_max = ''
        
#Ищу самое короткое из найденных
MinWord=word_min_len[0]
for i in range(len(word_min_len)):
    if len(word_min_len[i])<len(MinWord):
        MinWord=word_min_len[i]

#Ищу самое длинное из найденных
MaxWord=word_max_len[0]
for i in range(len(word_max_len)):
    if len(word_max_len[i])>len(MaxWord):
        MaxWord=word_max_len[i]
        
#Расстояние между ними
k=k1=k2=0
i=0
word=''
for i in range(len(s)):
    if (s[i]!=' ') and (s[i] not in clause_end) and (s[i] not in clause_cont):
        word += s[i]
    if (s[i] == ' ' or s[i] in clause_end) and word != '':
        k+=1
        if k1==0:
            if word==MaxWord: k1=k
        if k2==0:
            if word==MinWord: k2=k
        word=''
    
DistanceMinMax=abs(int(k1)-int(k2))

print('\nСамое короткое слово :', MinWord)
print('\nСамое длинное слово :', MaxWord)
print('\nРасстояние между ними :',DistanceMinMax-1)

#Разбиваем тескт на предложения
ArraySen=[]
Sentence=''
for i in range(len(s)):
    if s[i]!='.':
        Sentence+=s[i]
    else:
        Sentence+=s[i]
        ArraySen.append(Sentence)
        Sentence=''

#Ищем повторные слова
word=''
RepeatWords=[]
i=0
j=0
s1=''
for i in range(len(s)):
    A=True
    if s[i] != ' ':
        word+=s[i]
    else:
        for j in range(len(ArraySen)):
            s1=ArraySen[j]
            if s1.find(word)==-1:
                A=False
        if A==True:
            RepeatWords.append(word)
        word=''
print() 
print('Повторяющиеся слова: ')
for i in range(len(ArraySen)):
    print(RepeatWords[i],' ',end='')
print()
    
    

# Замена одного слова другим во всем тексте
old_word = input('\nВведите слово, которое заменяем: ')
new_word = input('Введите слово, на которое заменяем: ')
L_ow = len(old_word)
s1=''
k=0
s2=''
for i in range(len(s)):
    if s[i] != ' ':
        word+=s[i]
    else:
        if word==old_word:
            s2=s[k:i-len(word)]
            s1+=s2+new_word+' '
            k=i
        word=''
print('Измененный текст: ')
print(s1)
t=-1
# Удаление слова из первого предложения
word_del = input('\nВведите слово, которое удаляем из первого предложения: ')
L = len(word_del)
for k in range(len(text_2)):
    s = text_2[k]
    q = 0
    while q < len(s):
        if s[q] == ' ' and s[q-1] in clause_end:
            t = -1
            break
        if s[q:q+L] == word_del and s[q-1] == ' ' and (s[q+L] == ' ' or
            s[q+L] in clause_end or  s[q+L] in clause_cont):
            s = s[:q] + s[q+L:]
        q += 1
            
    text_2[k] = s
    if t == -1:
        break

print('\nИзмененный текст:\n')
for string in text_2:
    print(string)

