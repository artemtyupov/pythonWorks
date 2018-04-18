
# Найти некоторые значения и сделать преобразования массива
# С функциями

'''n = int(input('Введите количество строк: '))
text_1 = ['']*n
print('\nВведите массив строк:')
for i in range(n):
    text_1[i] = input()'''

text_1 = ['Крошечные котики ели ели ели ели крошечные тортики. Любят тортики',
          'крошечные котики! Лапками котики крошили',
          'тортики. Котики от тортиков наполнили животики?',
          '4*5+2.']

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
clause_cont = ',;:-'

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

# Поиск самых коротких слов в каждом предложении
word = ''
word_min_len = []
word_min_char = 0
for i in range(len(s)):
    if (s[i] != ' ') and (s[i] not in clause_end) and (s[i] not in clause_cont):
        word += s[i]
    if (s[i] == ' ' or s[i] in clause_end) and word != '':
        if len(word) < word_min_char or word_min_char == 0:
            word_min_char = len(word)
            word_min = word
        word = ''
    if s[i] in clause_end:
        word_min_len.append(word_min)
        word_min_char = 0
        word = ''
        word_min = ''

print('\nКоличество слов в каждой строке:', string_count_word)
print('\nСамое короткое слово в каждом предложении:', word_min_len)

# Поиск слова, которое наиболее часто встречается в первых двух строках
string = text_2[0]+text_2[1]
k = 0
count_max = 0
s = ''
s_need = ''
s1 = ''
for i in range(len(string)):
    if (string[i] != ' ') and (string[i] not in clause_end) and (
        string[i] not in clause_cont):
        s += string[i]
    
    if (string[i]== ' ' or string[i] in clause_end) and s != '':
        # Считаю, сколько раз обнаруженное слово встречается в строке
        for j in range(len(string)):
             if  (string[j] != ' ') and (string[j] not in clause_end) and (
                 string[j] not in clause_cont):
                 s_need += string[j]
             if  (string[j]== ' ' or string[j] in clause_end)  and s != '':
                 if s_need[1:] == s[1:]:
                     k += 1
                 s_need = ''
                 
        # Сравниваю частоту встречавшихся слов
        if k > count_max:
            count_max = k
            s1 = s
        k = 0
        s = ''       
print('\n\'',s1,'\' - слово, которое наиболее часто ',
      'встречается в первых двух строках', sep = '')

# Замена одного слова другим во всем тексте
old_word = input('\nВведите слово, которое заменяем: ')
new_word = input('Введите слово, на которое заменяем: ')
L_ow = len(old_word)
for i in range(len(text_2)):
    while old_word in text_2[i]:
        j = text_2[i].index(old_word)
        text_2[i] = text_2[i].replace(old_word, new_word)

print('\nИзменненый текст:\n')
for string in text_2:
    print(string)
print('DFDSGGDFSGDSFG',t)
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

input('\nЧтобы выйти из программы, нажмите Enter:')
