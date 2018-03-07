sayi = int(input("Sayiyi giriniz: "))
sayi2 = sayi
deger = 0

while(sayi > 0):
    mod = sayi % 10
    sayi = int(sayi / 10)
    deger += mod ** 3

if sayi2 == deger:
    print("Sayi armstrong sayidir")
else:
    print("Sayi armstrong sayi degildir")

