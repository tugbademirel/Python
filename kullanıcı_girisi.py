print("""
******************************
Kullanıcı Girişi Programı
******************************
""")

aa_kullanıcı_adı = "ttugba"
aa_parola = "321654"
giriş_hakkı = 3

while True:
    kullanıcı_adı = input("Kullanıcı Adı:")
    parola = input("Parola:")

    if (kullanıcı_adı != aa_kullanıcı_adı and parola == aa_parola ):
        print("Kullanıcı Adı Hatalı..")
        giriş_hakkı -= 1
    elif (kullanıcı_adı == aa_kullanıcı_adı and parola != aa_parola ):
        print("Parola Hatalı..")
        giriş_hakkı -= 1
    elif (kullanıcı_adı != aa_kullanıcı_adı and parola != aa_parola ):
        print("Kullanıcı adı ve Parola Hatalı..")
        giriş_hakkı -= 1
    else:
        print ("Sisteme Başarıyla Giriş Yaptınız...")
        break
    if (giriş_hakkı == 0 ):
        print ("Giriş Hakkınız Bitti...")
        break


