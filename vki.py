boy=float(input("boyunuzu m cinsinden girin : "))
kilo=int(input("lütfen kilonuzu kg cinsinden girin : "))
sonuc=kilo/(boy*boy)

if sonuc<18:
    print("zayif")
elif sonuc>=18 and sonuc<25:
    print("normal")
elif sonuc>=25 and sonuc<30:
    print("kilolu")
elif sonuc>=30 and sonuc<35:
    print("obez")
else:
    print("ciddi obez")
