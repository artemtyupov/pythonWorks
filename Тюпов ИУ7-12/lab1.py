#Тюпов Артем.
#Найти объем и площадь поверхности усеченной сферы.
from math import pi

if __name__ == "__main__":
    #Вводятся радиус-r и две высоты усеченных частей-h1,h2.
    r="a"
    h1="b"
    h2="c"
    while r.isalpha() or h1.isalpha() or h2.isalpha() or float(r)<=0 or float(h1)<=0 or float(h2)<=0:
        try:
            r = input("Введите радиус: ")
            r = float(r)
            h1 = input("Введите высоту первой отсеченной части: ")
            h1 = float(h1)
            h2 = input("Введите высоту второй отсеченной части: ")
            h2 = float(h2)
        except ValueError:
            print('Пишите цифры')
        
    V1 = (1/3)*pi*h1*h1*(3*r-h1)
    V2 = (1/3)*pi*h2*h2*(3*r-h2)
    V3 = (4/3)*pi*r*r*r    
    V = V3-V1-V2
    S1= 2*pi*r*h1
    S2= 2*pi*r*h2
    S3= 4*pi*r*r
    S= S3-S1-S2+2*pi*(r-h1)*(r-h2)
    print('Площадь поверхности сферы: {:5.3f}'.format(S))
    print("Объем сферы: {:5.3f}".format(V))
    
