# Жумабаев Султан ИУ7-13
# Найти некоторые значения и сделать преобразования массива
# Без функций

'''n = int(input('Введите количество строк: '))
text_1 = ['']*n
print('\nВведите массив строк:')
for i in range(n):
    text_1[i] = input()'''

text_1 = ['крошечные котики ели ели тортики. любят тортики',
          'крошечные котики. лапками котики крошили',
          'тортики. котики от тортиков наполнили животики.',
          '9+2*3 куриц. ']

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

def string_max(text):
    string_max = 0
    for s in text:
        if len(s) > string_max:
            string_max = len(s)
    return string_max

def reform_right(text):
    for s in text:
        print('\t' + ' '*(string_max(text) - len(s)) + s)


def cut(a, i, j, inp = ''):
    s = ''
    t = 0
    while t < i: 
        s += a[t]
        t += 1
    s += inp
    while j < len(a):
        s += a[j]
        j += 1
    return s

        
def result(s, znak):
    number = '0123456789'
    i=1
    while i < len(s) - 1:
        if s[i] == znak and s[i-1] in number and s[i+1] in number:
            k1 = k2 = ''
            
            t = i - 1
            while s[t] in number:
                k1 += s[t]
                t -= 1
            
            k11 = ''
            for j in range(len(k1)-1, -1, -1):
                k11 += k1[j]

            q = i + 1
            while s[q] in number:
                k2 += s[q]
                q += 1
                
            if znak == '*':       
                s = cut(s, t+1, q, str(int(k11)*int(k2)))
            elif znak == '+':
                s = cut(s, t+1, q, str(int(k11)+int(k2)))        
        i+=1
    return s

clause_end = '.?!'
clause_cont = ',;:-'

# Форматируем количество пробеллов между словами
for j  in range(len(text_1)):
    s = ''
    x = ' ' + text_1[j] + ' '
    for i in range(len(x)):
        if x[i] != ' ':
            s += x[i]
        elif x[i-1] != ' ':
            s += ' '
    text_1[j] = s

# Замена арифметического выражения (+*) на результат
for j in range(len(text_1)):
    text_1[j] = result(text_1[j],'*')
    text_1[j] = result(text_1[j],'+')

# Выравнивание строк по ширине
print('\nВыравнивание по ширине:\n')
n = 0
for x in text_1:
    print(format_width(x, 78))
    if n < len(x):
        n = len(x)
    
# Выравнивание строк по правому краю
print('\nВыравнивание по правому краю:\n')
reform_right(text_1)   

# Запись количества слов в каждой строке
print('\nКоличество слов в каждой строке: ',end=' ')
for i in range(len(text_1)):
    s = text_1[i]
    k = 0
    for j in range(len(s)):
        if s[j] == ' ':
            k += 1
    print(k, end=' ')


# Поиск самых коротких слов в каждом предложении
print('\nСамое короткое слово в каждом предложении:', end=' ')
s = ''
s_min =''
MIN = 0
for j in range(len(text_1)):
    c = text_1[j]
    for i in range(len(c)):
        if (c[i] != ' ') and (c[i] not in clause_end) and (c[i] not in clause_cont):
            s += c[i]
            
        if (c[i] == ' ' or c[i] in clause_end or c[i] in clause_cont) and s != '':
            if len(s) > MIN or MIN == 0:
                MIN = len(s)
                s_min = s
            s = ''
                
        if c[i] in clause_end:
            print(s_min, end=', ')
            s_min = ''
            MIN = 0

# Поиск слова, которое наиболее часто встречается в первых двух строках
s = text_1[0] + text_1[1]
k = 0
c = ''
cp = ''
count_max = 0
s1 = ''
for i in range(len(s)):
    if (s[i] != ' ') and (s[i] not in clause_end) and (s[i] not in clause_cont):
        c += s[i]
    
    if (s[i]== ' ' or s[i] in clause_end) and c != '':
        for j in range(len(s)):
             if (s[j] != ' ') and (s[j] not in clause_end) and (s[j] not in clause_cont):
                 cp+=s[j]
             if (s[j] == ' ' or s[j] in clause_end) and c != '':
                 if cp[1:] == c[1:]:
                     k += 1
                 cp = ''

        if k > count_max:
            count_max = k
            s1 = c
        k = 0
        c = ''
print('\n\'',s1,'\' - слово, которое наиболее часто ',
      'встречается в первых двух строках', sep = '')


# Замена одного слова другим во всем тексте
old = input('\nВведите слово, которое заменяем: ')
word=input('Введите слово, на которое заменяем: ')
L = len(old)

for j in range(len(text_1)):
    s = text_1[j]
    i = 0
    while i < len(s):
        if (s[i] != ' ') and (s[i] not in clause_end) and (s[i] not in clause_cont):
            c += s[i]
            
        if (s[i] == ' ' or s[i] in clause_end or s[i] in clause_cont) and c != '':
            if c == old:
                s = cut(s, i-L, i, word)
                i -= L - len(word)
            c = ''
        i += 1
    text_1[j] = s

print('\nИзменненый текст:\n')
for string in text_1:
    print(string)

# Удаление слова из первого предложения
w = input('\nВведите слово, которое хотите удалить из первого предложения: ')
L = len(w)
c = ''
t = 0
for i in range(len(text_1)):
    s = text_1[i]
    q = 0
    while q < len(s):
        if s[q] == ' ' and s[q-1] in clause_end:
            t = -1
            break
        
        if (s[q] != ' ') and (s[q] not in clause_end) and (s[q] not in clause_cont):
            c += s[q]
            
        if (s[q] == ' ' or s[q] in clause_end or s[q] in clause_cont) and c != '':
            if c == w:
                s = cut(s, q-L, q)
                q -= L
            c = ''
        q += 1
        
    text_1[i] = s
    
    if t == -1:
        break

print('\nИзменненый текст:\n')
for string in text_1:
    print(string)

input('\nЧтобы выйти из программы, нажмите Enter:')
