def SiraliEkle(deger,dizi):
    i = 0
    kontrol = 0
    if len(dizi) == 0:
        dizi.append(deger)
    else:
        while i<len(dizi):
            if deger < dizi[i]:
                dizi.insert(i,deger)
                kontrol = 1
                break
            i = i + 1
        if kontrol == 0:
            dizi.append(deger)




    #     for i in range(len(dizi)):
    #         if deger < dizi[i]:
    #             dizi.insert(i,deger)
    #             break
    #         elif i == len(dizi)-1:
    #             dizi.append(deger)
    #             break
    print(dizi)


dizi = []
for i in range(0,5):

    deger = int(input("Sayi giriniz: "))
    SiraliEkle(deger,dizi)