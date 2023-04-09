tutulan_sayi = 4
tahmin_hakki = 2
print("1 ile 10 arasında bir sayı tuttum. Bunu bul ! "+str(tahmin_hakki)+" hakkın var")
while tahmin_hakki != 0:

    tahmin_edilen_sayi = int(input("sayı tahmini:"))
    if (tahmin_edilen_sayi < 1 or tahmin_edilen_sayi > 10):
        print("Lütfen 1 ile 10 arasında bir sayı giriniz!")
        continue

    if (tahmin_edilen_sayi == tutulan_sayi):
        print("tahmin doğru")
        break

    elif (tahmin_edilen_sayi != tutulan_sayi):
        tahmin_hakki = tahmin_hakki - 1
        print("tahmin yanlış kalan hak: "+str(tahmin_hakki)+" ")
        if (tahmin_hakki == 0):
            print("tahmin hakkınız bitti..")

