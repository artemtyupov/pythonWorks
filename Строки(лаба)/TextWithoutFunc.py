# Тюпов Артем ИУ7-12
# Версия программы без использования функций

text_1 = ['ПОВТОР Python 2+2 поддерживает несколько парадигм программирования',
          'в том числе структурное, объектно-ориентированное, функциональное,',
          'императивное, выгодное и аспектно-ориентированное. ПОВТОР Основные архитектурные',
          'черты - динамическая типизация,',
          'автоматическое управление памятью, полная интроспекция, механизм обработки',
          'исключений,поддержка многопоточных вычислений и удобные высокоуровневые',
          'структуры данных. 2*2 ПОВТОР Код в Python организовывается в функции и классы,',
          'которые могут объединяться в модули они в свою очередь могут быть',
          'объединены в различные многофункциональные пакеты 3*4']


#Функция len1 собственно
def len1(string):
    i=0
    for k in string:
        i+=1
    return i
def ClauseEnd(char):
    clause_end = '.?!'
    A=True
##    for i in range(len1(clause_end)):
##        for j in range(len1(char)):
##            if clause_end[i]!=char[j]:
##                A=False
    if char in clause_end:
        return True
    else:
        return False
def Number(char):
    number = '0123456789'
    if char in number:
        return True
    else:
        return False
def ClauseCont(char):
    clause_cont = ',;:—'
    if char in clause_cont:
        return True
    else:
        return False
        
# Функция выравнивания текста по правому краю
def reform_right(text):
    len1_max_string = 0
    for string in text:
        if len1(string) > len1_max_string:
            len1_max_string = len1(string)
    for string in text:
        print('\t' + ' '*(len1_max_string-len1(string)) + string)

# Функция выравнивания по ширине
def format_width(string, n):
    a = string.split()
    l = 0
    for x in a:
        l+= len1(x)
    if len1(a) > 1:
        spaces = int((n-l)/(len1(a)-1))
        extra = n-l-spaces*(len1(a)-1)-1
        result = a[0] + ' '*(spaces+1)
        for i in range(1,len1(a)-1):
            if extra > 0:
                result += a[i]
                for x in range(spaces+1):
                    result += ' '
                extra-=1
            else:
                result+= a[i] + ' '*spaces
        return result + a[len1(a)-1]
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
    for i in range(1,len1(string)):
        if string[i] != ' ':
            s += string[i]
        elif string[i-1] != ' ':
            s += ' '
            k += 1
    string_count_word.append(k)
    text_2.append(s)
    
# Замена арифметического выражения (+*) на результат
number = '0123456789'
for j in range(len1(text_2)):
    s = text_2[j]
    i = 1
    while i < len1(s)-1:
        if s[i] == '*' and Number(s[i-1]) and Number(s[i+1]):
            k1 = k2 = ''
            t = i - 1
            q = i + 1
            while Number(s[t]):
                k1 += s[t]
                t -= 1
            k1 = k1[::-1]
            while Number(s[q]):
                k2 += s[q]
                q += 1
            s = s[:t+1] + str(int(k1)*int(k2)) + s[q:]
            
        if s[i] == '+' and Number(s[i-1]) and Number(s[i+1]):
            k1 = k2 = ''
            t = i - 1
            q = i + 1
            while Number(s[t]):
                k1 += s[t]
                t -= 1
            k1 = k1[::-1]
            while Number(s[q]):
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
    if n < len1(x):
        n = len1(x)

# Переписываю весь текст в одну строку
s = ''
for string in text_2:
    s += string

# Поиск самых коротких и самых длинных слов в каждом предложении
word = ''
word_min_len1 = []
word_min_char = 0
word_max_char = 0
word_max_len1=[]
for i in range(len1(s)):
    if (s[i]!=' ') and (not ClauseEnd(s[i])) and (not ClauseCont(s[i])):
        word += s[i]
    if (s[i] == ' ' or ClauseEnd(s[i])) and word != '':
        if len1(word) < word_min_char or word_min_char == 0:
            word_min_char = len1(word)
            word_min = word
        if len1(word) > word_max_char or word_max_char == 0:
            word_max_char = len1(word)
            word_max = word
        word = ''
    if ClauseEnd(s[i]):
        word_min_len1.append(word_min)
        word_min_char = 0
        word_max_len1.append(word_max)
        word_max_char = 0
        word = ''
        word_min = ''
        word_max = ''
        
#Ищу самое короткое из найденных
MinWord=word_min_len1[0]
for i in range(len1(word_min_len1)):
    if len1(word_min_len1[i])<len1(MinWord):
        MinWord=word_min_len1[i]

#Ищу самое длинное из найденных
MaxWord=word_max_len1[0]
for i in range(len1(word_max_len1)):
    if len1(word_max_len1[i])>len1(MaxWord):
        MaxWord=word_max_len1[i]
        
#Расстояние между ними
k=k1=k2=0
i=0
word=''
for i in range(len1(s)):
    if (s[i]!=' ') and (not ClauseEnd(s[i])) and (ClauseCont(s[i])):
        word += s[i]
    if (s[i] == ' ' or ClauseEnd(s[i])) and word != '':
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
for i in range(len1(s)):
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
for i in range(len1(s)):
    A=True
    if s[i] != ' ':
        word+=s[i]
    else:
        for j in range(len1(ArraySen)):
            s1=ArraySen[j]
            if s1.find(word)==-1:
                A=False
        if A==True:
            RepeatWords.append(word)
        word=''
print() 
print('Повторяющиеся слова: ')
for i in range(len1(ArraySen)):
    print(RepeatWords[i],' ',end='')
print()
    
    

# Замена одного слова другим во всем тексте
old_word = input('\nВведите слово, которое заменяем: ')
new_word = input('Введите слово, на которое заменяем: ')
L_ow = len1(old_word)
s1=''
k=0
s2=''
for i in range(len1(s)):
    if s[i] != ' ':
        word+=s[i]
    else:
        if word==old_word:
            s2=s[k:i-len1(word)]
            s1+=s2+new_word+' '
            k=i
        word=''
print('Измененный текст: ')
print(s1)
t=-1
# Удаление слова из первого предложения
word_del = input('\nВведите слово, которое удаляем из первого предложения: ')
L = len1(word_del)
for k in range(len1(text_2)):
    s = text_2[k]
    q = 0
    while q < len1(s):
        if s[q] == ' ' and ClauseEnd(s[q-1]):
            t = -1
            break
        if s[q:q+L] == word_del and s[q-1] == ' ' and (s[q+L] == ' ' or
            ClauseEnd(s[q+L]) or  ClauseCont(s[q+L])):
            s = s[:q] + s[q+L:]
        q += 1
            
    text_2[k] = s
    if t == -1:
        break

print('\nИзмененный текст:\n')
for string in text_2:
    print(string)


