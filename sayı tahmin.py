

a=int(input("baþlamak için 1 tuþuna çýkýþ yapmak için 2 tuþuna basýnýz : "))

    
def sayitahmin():
    
    from random import randint
    sayi=randint(1,100)

    sayac=0     #kullanicinin tahmin sayisini bulabilmek için bir sayaç oluþturduk ve baþlangýç deðeri olarak 0 verdik.
    tahmin=int(input("1 ile 100 arasýnda bir sayý girin : "))
    while True:
        
        if tahmin<sayi:
            print("daha yüksek bir sayý gir")
            sayac+=1          #sayaci 1 arttirdik çünkü kullanici tahminde bulundu.
            tahmin=int(input("1 ile 100 arasýnda bir sayý girin : "))


        elif tahmin>sayi:
            print("daha küçük bir sayý gir")
            sayac+=1
            tahmin=int(input("1 ile 100 arasýnda bir sayý girin : "))


        elif tahmin==sayi:
            sayac+=1
            print("tebrikler doðru bildiniz")
            print("tahmin sayýnýz : {}".format(sayac))
            break        #ekrana sürekli ayný þeyi yazdýrmamasý için "break" yazdýk.

while True:
    if a==1:
        sayitahmin()
        a=int(input("baþlamak için 1 tuþuna çýkýþ yapmak için 2 tuþuna basýnýz : "))
        
    elif a==2:
        print("çýkýþ yapýlýyor")
        break
