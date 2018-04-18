#Тюпов Артем ИУ7-22
        
def create():
    file = open("g2.txt", "w")
    file.close()

    
    
def check(k1,k2):
    file = open("g1.txt")
    line = file.readline()
    n = 2
    line1 = ''
    line2 = ''
    while line:
        line = file.readline()
        if n == k1: line1 = line
        if n == k2: line2 = line
        n += 1
    if line1 == line2: return 0
    if line1 != line2: return 1


    
def writing(i):
    file1 = open("g1.txt")
    file2 = open("g2.txt", "a")
    line = file1.readline()
    n = 1
    while line:
        print(n,i)
        if n == i:
            file2.write(line)
            break
        line = file1.readline()
        n += 1
        
    
            
create()
file = open("g1.txt")
line_old = file.readline()
n = 1
while line_old:
    line_old = file.readline()
    n += 1
for i in range(0,n-1):
    Flag2 = 1
    for j in range(i,n):
        Flag = check(i,j)
        print(Flag)
        if Flag == 0 :
            Flag2 = 0
    if Flag2 == 0:
        writing(i)
        

    
