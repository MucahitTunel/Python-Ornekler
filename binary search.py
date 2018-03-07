def bul(dizi, aranan):

    print(dizi)
    if len(dizi) == 1:
        if dizi[0] != aranan:
            print("Böyle bir değer bulunmamaktadır")
            exit(-1)
    uzunluk = len(dizi)
    orta = int(uzunluk / 2)
    if dizi[orta] == aranan:
        print("Tebrikler buldunuz")
        exit(-1)
    elif dizi[orta] > aranan:
        return bul(dizi[0:orta],aranan)
    elif dizi[orta] < aranan:
        return bul(dizi[orta+1:],aranan)
    else:
        print("Böyle bir değer bulunmamaktadır")
        exit(-1)






dizi = [1,4,2,6,7,9,3,22,16]

dizi = sorted(dizi)

aranan = int(input("Aranan deger: "))

bul(dizi, aranan)
