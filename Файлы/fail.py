#Артем Тюпов ИУ7-22


#Функция создания файла
def create():
    print('-'*40)
    file_name = input('Введите имя нового файла: ')
    file = open(file_name, "w")
    file.close()

#Функция записи    
def writefile():
    print('-'*40)
    length_column = 30                        
    file_name = input('Введите имя нужного файла: ')
    file = open(file_name, "a")
    print('Выход = 0')
    print('Добавление новой записи = 1')
    menu_number = int(input('Для выбора пункта введите указанную цифру: '))
    while menu_number != 0:
        brand = input('Введите название бренда: ')
        country = input('Введите название страны: ')
        file.write(brand+(length_column-len(brand))*' '+country+'\n')
        print('Запись добавлена, для выхода введите 0')
        print('Для продолжения работы введите 1')
        menu_number = int(input())
    file.close()

#Функция поиска    
def find():
    file_name = input('Введите имя нужного файла: ')
    file = open(file_name, "r")
    menu_number = -1
    find_flag = -1
    while menu_number != 0:
        print('-'*40)
        print('Выход = 0')
        print('Поиск по названию бренда = 1')
        print('Поиск по названию страны = 2')
        print('Поиск по ключевому слову = 3')
        menu_number = int(input('Для выбора пункта введите указанную цифру: '))
        if menu_number == 1:
            find_brand = input('Введите имя искомоого бренда: ')
            line = file.readline()
            while line:
                line = file.readline()
                flag = line.find(find_brand)
                if (flag != -1) and (flag <= 30):
                    if find_flag != 1:
                        file_new = open('find_result.txt', "w")
                        file_new.close()
                        file_new = open('find_result.txt', "a")
                        file_new.write(line)
                        file_new.close()
                        find_flag = 1
                    else:
                        file_new = open('find_result.txt', "a")
                        file_new.write(line)
                        file_new.close()
        elif menu_number == 2:
            find_country = input('Введите имя искомой страны: ')
            line = file.readline()
            while line:
                line = file.readline()
                flag = line.find(find_country)
                if (flag != -1) and (flag >= 30):
                    if find_flag != 1:
                        file_new = open('find_result.txt', "w")
                        file_new.close()
                        file_new = open('find_result.txt', "a")
                        file_new.write(line)
                        file_new.close()
                        find_flag = 1
                    else:
                        file_new = open('find_result.txt', "a")
                        file_new.write(line)
                        file_new.close()
        elif menu_number == 3:
            find_word = input('Введите имя искомого слова: ')
            line = file.readline()
            while line:
                line = file.readline()
                flag = line.find(find_word)
                if (flag != -1):
                    if find_flag != 1:
                        file_new = open('find_result.txt', "w")
                        file_new.close()
                        file_new = open('find_result.txt', "a")
                        file_new.write(line)
                        file_new.close()
                        find_flag = 1
                    else:
                        file_new = open('find_result.txt', "a")
                        file_new.write(line)
                        file_new.close()

#функция вывода исходного файла                        
def show():
    print('-'*40)
    file_name = open('Brand.txt', "r")
    line = file_name.readline()
    while line:
        line = file_name.readline()
        print(line)


#Главная часть
menu_number = -1
while menu_number != 0:
    print('-'*40)
    print('Выход = 0')
    print('Создание нового файла = 1')
    print('Добавить записей к файлу = 2')
    print('Поиск в файле = 3')
    print('Вывести исходный файл = 4')
    menu_number = int(input('Для выбора пункта введите указанную цифру: '))
    if menu_number == 1:
        create()
    elif menu_number == 2:
        writefile()
    elif menu_number == 3:
        find()
    elif menu_number == 4:
        show()
quit
            
            
        
