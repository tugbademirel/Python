a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

birinci_kok = (-b+(b**2-4*a*c**0.5))/(2*a)
ikinci_kok = (-b-(b**2-4*a*c**0.5))/(2*a)

print("Birinci Kök: {} \nİkinci Kök: {}".format(birinci_kok, ikinci_kok))

