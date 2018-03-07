def diziler(x,y,z):
    yenidizi = x + y + z
    dizi = []
    deger = int(len(yenidizi) / 3)
    k = 0
    for i in range(deger):

        dizi.append([yenidizi[k], yenidizi[k+1], yenidizi[k+2]])
        k += 3


    print(dizi)




x = [1,2,3,4,5]
y = [6,7,8,9,10]
z = [11,12,13,14,15]

diziler(x,y,z)

