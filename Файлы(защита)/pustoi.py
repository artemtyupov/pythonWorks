#Тюпов Артем ИУ7-22

file1 = open("students.txt")
file2= open("studentsNEW.txt", "w")
file2.close()
file2= open("studentsNEW.txt", "a")
line = file1.readline()
k1 = k2 = k3 = 0
while line:
    k1 += 1
    if line.rfind('2') == -1:
        k2 += 1
        file2.write(line)
    line = file1.readline()
k3 = k1 - k2
print('Количество хвостистов: ',k3)
file2.close()
file1.close()
        
