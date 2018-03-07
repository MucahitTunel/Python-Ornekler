liste = [11,2,33,5,6,7,4,2,8,4,5,9]

artan = 0
azalan = 0
aynı = 0
çift = 0
tek = 0

for i in range(0,len(liste)-1):
    j = i+1
    if liste[i] > liste[j]:
        azalan += 1
    elif liste[j] > liste[i]:
        artan += 1
    else:
        aynı += 1

    if liste[i] % 2 == 0 and liste[j] % 2 == 0:
        çift += 1
    if liste[i] % 2 == 1 and liste[j] % 2 == 1:
        tek += 1

print("Tek: %d"%(tek))
print("Çift: %d"%(çift))
print("Artan: %d"%(artan))
print("Azalan: %d"%(azalan))



