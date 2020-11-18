import os
import time
bakiye=3000

while True:
    os.system("cls")
    print("**********\nBankaPy hizmet ekranına hoşgeldiniz...\npara çekme : <1>\npara yatırma : <2>\nbakiye sorgulama : <3>\nçıkış yap : <q>\n********************")
    secim=input("gerçekleştirmek istediğiniz işlemi seçin : ")

    if secim=="1":
        cek=int(input("çekmek istediğiniz miktarı girin : "))
        if (bakiye-cek)<0:
            print("yetersiz bakiye")
            time.sleep(2)
            continue
        
        bakiye-=cek
        print("{} TL çekildi".format(cek))
        print("kalan bakiyeniz : {}".format(bakiye))
        time.sleep(2)
        continue
    elif secim=="2":
        yatır=int(input("yatırmak istediğiniz miktarı girin : "))
        bakiye+=yatır
        print("{} TL yatırıldı".format(yatır))
        print("toplam bakiyeniz : {}".format(bakiye))
        time.sleep(2)
        continue
    elif secim=="3":
        
        print("toplam bakiyeniz : {}".format(bakiye))
        time.sleep(2)
        continue
    elif secim=="q" or secim=="Q":
        print("çıkış yapılıyor......")
        time.sleep(2)
        break
    else:
        print("lütfen varilen bilgiler dışında giriş yapmayın")
        time.sleep(2)
        continue


















    
      
