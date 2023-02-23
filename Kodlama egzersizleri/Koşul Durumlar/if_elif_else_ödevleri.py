"""
Problem 1
Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu kurallara göre ekrana şu yazıları yazdırın.
 Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)
 BKİ 18.5'un altındaysa -------> Zayıf
 BKİ 18.5 ile 25 arasındaysa ------> Normal
 BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu
 BKİ 30'un üstündeyse -------------> Obez
"""


#print("""*********************
#Beden Kitle Endeksi Hesaplama
#*********************""")
"""
boy = float(input("Boyunuz:"))
kilo = int(input("Kilonuz:"))

beden_kitle_endeksi = kilo / boy ** 2


if (beden_kitle_endeksi < 18.5):
    print("Zayıf")
elif (beden_kitle_endeksi >= 18.5 and beden_kitle_endeksi < 25):
    print("Normal")
elif (beden_kitle_endeksi >= 25 and beden_kitle_endeksi < 30):
    print("Fazla kilolu")
else:
    print("Obez")

#Problem 2 -- Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.
"""
"""
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

if (a >= b and a >= c):
    print("En büyük sayı:",a)
elif (b >= a and b>= c):
    print("En büyük sayı:",b)
elif (c >= a and c >= b):
    print("En büyük say:",c)
"""

"""
Problem 3
Kullanıcının girdiği vize1,vize2,final notlarına notlarına göre harf notunu hesaplayın.
Vize1 toplam notun %30'una etki edecek.
Vize2 toplam notun %30'una etki edecek.
Final toplam notun %40'ına etki edecek
"""

"""
vize1 = int(input("1.Vize:"))
vize2 = int(input("2.Vize:"))
final = int(input("Final Notu:"))

toplam_not = (vize1 * 30 /100) + (vize2 * 30 / 100) + (final * 40 /100)

print("Toplam not:",toplam_not)

if(toplam_not >= 90):
    print("Harf notunuz: AA")
elif(toplam_not >= 85):
    print("Harf notunuz: BA")
elif(toplam_not >= 80):
    print("Harf notunuz: BB")
elif(toplam_not >= 75):
    print("Harf notunuz: CB")
elif(toplam_not >= 70):
    print("Harf notunuz: CC")
elif(toplam_not >= 65):
    print("Harf notunuz: DC")
elif(toplam_not >= 60):
    print("Harf notunuz: DD")
elif(toplam_not >= 55):
    print("Harf notunuz: FD")
else:
    print("Harf notunuz: FF")
"""

"""
Problem 4 Şimdi de geometrik şekil hesaplama işlemi yapalım. 
İlk olarak kullanıcıdan üçgenin mi dörtgenin mi tipini bulmak istediğini sorun.
Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi , 
  dikdörtgen mi yoksa sıradan bir dörtgen mi olduğunu bulmaya çalışın.

"""

şekil = input("Hangi şeklin tipini öğrenmek istersiniz?")

if (şekil == "Dörtgen"):
    print("Lütfen kenarları sırayla giriniz.")
    a = int(input("1.kenar:"))
    b = int(input("2.kenar:"))
    c = int(input("3.kenar:"))
    d = int(input("4.kenar:"))

    if( a == b and b == c and c == d):
        print("Kare")
    if( a == c and b == d):
        print("Dikdörtgen")
    else:
        print("Sıradan dörtgen")

elif (şekil == "Üçgen"):
    print("Kenarları sırayla giriniz:")
    a = int(input("1.Kenar:"))
    b = int(input("2.kenar"))
    c = int(input("3.Kenar"))
    if  ( abs(a+b) > c and abs(a+c) > b and abs(b+c) > a):
        if((a == b and a != c) or (a == c and a != b) or (b == c and b != a)):
            print("İkizkenar üçgen")
        elif(a == b and b == c):
            print("Eşkenar üçgen")
        else:
            print("Düz üçgen")

else:
    print("Geçersiz Şekil...")