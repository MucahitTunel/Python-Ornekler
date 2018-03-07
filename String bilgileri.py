metin = "Bu hatalar, programlama diline ilişkin bir özelliğin yanlış kullanımından veya en basit \
şekilde programcının yaptığı yazım hatalarından kaynaklanır. Programcının hataları genellikle \
SyntaxError şeklinde ortaya çıkar. Bu hatalar çoğunlukla programcı tarafından farkedilir ve \
program kullanıcıya ulaşmadan önce programcı tarafından düzeltilir. Bu tür hataların tespiti \
diğer hatalara kıyasla kolaydır. Çünkü bu tür hatalar programınızın çalışmasını engellediği \
için bunları farketmemek pek mümkün değildir"

liste = metin.split()
karakter = set(metin)

for kelime in set(liste):
    print("%s kelimesi %d kere bulunmaktadır."%(kelime, liste.count(kelime)))

for krkter in karakter:
    print("%s karakteri: %d "%(krkter, metin.count(krkter)))

