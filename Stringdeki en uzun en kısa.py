metin = "Daha sonra da kontrol değişkeninin durumuna göre kullanıcıya parolanın onaylandığı veya  \
onaylanmadığı bilgisini veriyoruz. Buna göre eğer kontrol değişkeninin değeri True ise şu  \
çıktıyı veriyoruz"

liste = metin.split()

print(liste)


print("En uzun kelime: %s"%(max(liste, key=len)))

print("En kısa kelime: %s"%(min(liste, key=len)))