

a=int(input("baslamak için 1 tusuna çikiþ yapmak için 2 tusuna basiniz : "))

    
def sayitahmin():
    
    from random import randint
    sayi=randint(1,100)

    sayac=0     #kullanicinin tahmin sayisini bulabilmek için bir sayaç olusturduk ve baslangiç degeri olarak 0 verdik.
    tahmin=int(input("1 ile 100 arasinda bir sayi girin : "))
    while True:
        
        if tahmin<sayi:
            print("daha yüksek bir sayi gir")
            sayac+=1          #sayaci 1 arttirdik çünkü kullanici tahminde bulundu.
            tahmin=int(input("1 ile 100 arasinda bir sayi girin : "))


        elif tahmin>sayi:
            print("daha küçük bir sayi gir")
            sayac+=1
            tahmin=int(input("1 ile 100 arasinda bir sayi girin : "))


        elif tahmin==sayi:
            sayac+=1
            print("tebrikler doðru bildiniz")
            print("tahmin sayiniz : {}".format(sayac))
            break        #ekrana sürekli ayni seyi yazmamasi için "break" kullandik.

while True:
    if a==1:
        sayitahmin()
        a=int(input("baslamak için 1 tusuna çikis yapmak için 2 tusuna basiniz : "))
        
    elif a==2:
        print("çikis yaptiniz")
        break
