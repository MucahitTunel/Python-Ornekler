mail = "sdasdas@gmail.com"


mail_uzunluk = len(mail)


if mail[mail_uzunluk-12:] == "@hotmail.com" or mail[mail_uzunluk-10:]=="@gmail.com":
    print("Doğru")

else:
    print("yanlis")