#Problem 1
#Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın.
#Ekrana yazdırma işlemini *format* metoduyla yapmaya çalışın.

"""
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

çarpım = a*b*c

print("{} * {} * {} = {} dir".format(a,b,c,çarpım))
"""

#Problem 2
#Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.
#Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)

""" 
boy = float(input("boy:"))
kilo = int(input("kilo:"))


print("Beden kitle endeksi:",kilo / (boy ** 2))
"""

"""
yakan_miktar = float(input("Kilometrede yakan miktar:"))

kilometre = int(input("Kaç km yol yaptınız:"))

print("Tutar: {} tl".format(yakan_miktar * kilometre))
"""

#Problem 4
#Kullanıcıdan ad,soyad ve numara bilgisini alarak bunları alt alta ekrana yazdırın.

"""
ad = input("Adınız:")
soyad = input("Soyadınız:")
numara = int(input("Numaranız:"))

print("\nBilgileriniz...\n")
print("{}\n{}\n{}\n".format(ad,soyad,numara))
"""

#Problem 5
#Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.

"""
a = int(input("a:"))
b = int(input("b:"))

print("Değiştirilmeden önceki değerler\n a: {} b: {}\n".format(a,b))
a,b = b,a
print("Değiştirildikten sonraki değerler\n a: {} b: {}\n".format(a,b))
"""

#Problem 6
#Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın.
#Hipotenüs Formülü: a^2 + b^2 = c^2

a = int(input("a:"))
b = int(input("b:"))

c = (a** 2 + b** 2 ) ** 0.5

print("Hipotenüs:",c)
