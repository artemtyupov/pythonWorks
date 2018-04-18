#Pisaruc Victor IU7-12
#Graffic func



hn = 0.05        #шаг
z = -1.70
sp = []
while z < -0.5:
    alph = z**9 + 3*z**8 - z**7 + z**6 + 6*z**5 - 7*z**4 + z**3 + z**2 - z +2
    print('При z ={:.5f} '.format(z),'функция alph = {:.5f}'.format(alph))
    sp.append(alph)
    z += 0.05
mn = min(sp)
mx = max(sp)
print()
print()
print()
print('При z = -1.35 , Минимум функции алфа = {:.5f} '.format(mn))
print('При z = -1.70 , Максимум функции алфа = {:.5f} '.format(mx))

    

