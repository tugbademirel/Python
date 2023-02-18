print("""**************************
      Kullanıcı Girişi
**************************""")

anbr_kullanıcı_adı = "ttugba"
anbr_parola = "123456"

kullanıcı_adı = input("Kullanıcı Adı:")
parola= input("Parola:")

if (kullanıcı_adı == anbr_kullanıcı_adı and parola != anbr_parola):
    print("Parolanız Hatalı...")
elif (kullanıcı_adı != anbr_kullanıcı_adı and parola == anbr_parola):
    print("Kullanıcı Adı Hatalı...")
elif (kullanıcı_adı != anbr_kullanıcı_adı and parola != anbr_parola):
    print("Kullanıcı Adı ve Parola Hatalı...")

else:
    print("Giriş Başarılı.....")