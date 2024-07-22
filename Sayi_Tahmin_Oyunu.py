print ("--SAYI TAHMİN OYUNU --")
import random
tahmin= int(input("Lütfen 1-10 arası bir  Sayı Tahmin ediniz:"))

import random
asil_sayi=random.randrange(1,10)
print("Asıl Sayı:",asil_sayi, "Tahmin ettiğinz sayı:",tahmin)


if tahmin ==asil_sayi:
    print("Tebrikler ! KAZANDINIZ !")
else:
    print("Malesef bilemediniz! Asıl sayı:",asil_sayi)