def bublesort(dizi):
    uzunluk = len(dizi) - 1
    for i in range(0,len(dizi)):
        for j in range(0,uzunluk):
            k = j+1
            if dizi[j] > dizi[k]:
                temp = dizi[j]
                dizi[j] = dizi[k]
                dizi[k] = temp
        uzunluk = uzunluk-1
        print(dizi)
dizi = [3,4,7,1,8,2,11,34,22]
bublesort(dizi)
