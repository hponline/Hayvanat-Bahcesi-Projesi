"""
*********** Yapılmak istenen proje ***********

Hayvanat Bahçesi Projesi
500'e 500'lük bir alanda yaşayan 30 koyun (15 erkek,15 dişi), 10 inek (5 erkek,5 dişi),
10 tavuk,10 kurt (5 dişi,5 erkek) 10 horoz, 8 aslan (4 erkek, 4 dişi) ve 1 avcı
bulunmaktadır.
Hayvanlardan;
koyun 2 birim,
kurt 3 birim,
inek 2 birim,
tavuk 1 birim,
horoz 1 birim,
aslan 4 birim,
avcı 1 birim rasgele şekilde hareket etmektedir ancak alanın dışına çıkamamaktadır.
kurt kendisine 4 birim yakınındaki koyun, tavuk, horoz'u avlayabiliyor.
aslan kendisine 5 birim yakınlıktaki inek, koyun'u avlayabiliyor.
avcı da kendisine 8 birim yakınlıktaki hayvanlardan herhangi birisini avlayabiliyor.
aynı cins farklı cinsiyetteki hayvanlar birbirine 3 birim yakınlaştığı zaman random
cinsiyetli ve aynı cins bir hayvan meydana gelmektedir.
1000 birim hareket sonunda hayvanların sayısının bulunduğu bir console application
yazılması beklenmektedir.
"""

import random

class Arazi:
    def __init__(self, arazi_En=500, arazi_Boy=500):
        self.arazi_En = arazi_En
        self.arazi_Boy = arazi_Boy

class Hayvan:
    def __init__(self, konumX, konumY, tür, birim, cinsiyet=None):
        self.konumX = konumX
        self.konumY = konumY
        self.tür = tür
        self.birim = birim
        self.cinsiyet = cinsiyet

    # Hareket fonksiyonu
    def hareket_et(self, arazi):
        yeni_konumX = self.konumX + random.randint(-1, 1)
        yeni_konumY = self.konumY + random.randint(-1, 1)
        self.konumX = max(0, min(arazi.arazi_En, yeni_konumX))
        self.konumY = max(0, min(arazi.arazi_Boy, yeni_konumY))
    
    # Avlanma başarılı olabilmesi için av ile avcı arasındaki birim hesabı    
    def mesafe_hesapla(self, diger_hayvan):
        return ((self.konumX - diger_hayvan.konumX) ** 2 + (self.konumY - diger_hayvan.konumY) ** 2) ** 0.5

class Koyun(Hayvan):
    def __init__(self, konumX, konumY, cinsiyet=None):
        super().__init__(konumX, konumY, tür="Koyun", birim=2)
        self.cinsiyet = cinsiyet

class Kurt(Hayvan):
    def __init__(self, konumX, konumY, cinsiyet=None):
        super().__init__(konumX, konumY, tür="Kurt", birim=3)
        self.cinsiyet = cinsiyet

    def avla(self, hayvanlar):
        for hayvan in hayvanlar:
            mesafe = self.mesafe_hesapla(hayvan)
            if mesafe <= 4 and hayvan.tür != "Kurt":
                print(f"{self.tür} yakınındaki {hayvan.tür} avlandı!")
                hayvanlar.remove(hayvan)
                return

class Inek(Hayvan):
    def __init__(self, konumX, konumY, cinsiyet=None):
        super().__init__(konumX, konumY, tür="Inek", birim=2)
        self.cinsiyet = cinsiyet

class Tavuk(Hayvan):
    def __init__(self, konumX, konumY):
        super().__init__(konumX, konumY, tür="Tavuk", birim=1)

class Horoz(Hayvan):
    def __init__(self, konumX, konumY):
        super().__init__(konumX, konumY, tür="Horoz", birim=1)

class Aslan(Hayvan):
    def __init__(self, konumX, konumY, cinsiyet=None):
        super().__init__(konumX, konumY, tür="Aslan", birim=4)
        self.cinsiyet = cinsiyet

    def avla(self, hayvanlar):
        for hayvan in hayvanlar:
            mesafe = self.mesafe_hesapla(hayvan)
            if mesafe <= 5 and hayvan.tür != "Aslan":
                print(f"{self.tür} yakınındaki {hayvan.tür} avlandı!")
                hayvanlar.remove(hayvan)
                return

class Avci(Hayvan):
    def __init__(self, konumX, konumY):
        super().__init__(konumX, konumY, tür="Avci", birim=1)

    def hareket_et(self, arazi):
        yeni_konumX = self.konumX + random.randint(-1, 1)
        yeni_konumY = self.konumY + random.randint(-1, 1)
        self.konumX = max(0, min(arazi.arazi_En, yeni_konumX))
        self.konumY = max(0, min(arazi.arazi_Boy, yeni_konumY))

    def avla(self, hayvanlar):
        for hayvan in hayvanlar:
            mesafe = self.mesafe_hesapla(hayvan)
            if mesafe <= 8 and hayvan.tür != "Avci":
                print(f"{self.tür} yakınındaki {hayvan.tür} avlandı!")
                hayvanlar.remove(hayvan)
                return
              
# Hayvan sınıfımız
class HayvanOlusturma:
    def __init__(self, arazi):
        self.arazi = arazi
        self.hayvanlar = []
    
    # Üreme çalışmıyor.
    def ureme_kontrol(self):
            for hayvan1 in self.hayvanlar:
                for hayvan2 in self.hayvanlar:
                    if hayvan1 != hayvan2 and hasattr(hayvan1, 'cinsiyet') and hasattr(hayvan2, 'cinsiyet'):
                        mesafe = hayvan1.mesafe_hesapla(hayvan2)
                        if mesafe <= 3 and type(hayvan1) == type(hayvan2) and hayvan1.cinsiyet != hayvan2.cinsiyet:
                            self.ureme_gercekles(hayvan1, hayvan2)
    
    # Üreme çalışmıyor.    
    def ureme_gercekles(self, hayvan1, hayvan2):
        yeni_hayvan = type(hayvan1)(random.randint(0, self.arazi.arazi_En), random.randint(0, self.arazi.arazi_Boy))
        yeni_hayvan.cinsiyet = random.choice([hayvan1.cinsiyet, hayvan2.cinsiyet])
        self.hayvanlar.append(yeni_hayvan)
        print(f"Yeni bir {yeni_hayvan.cinsiyet} {yeni_hayvan.tür} doğdu!")

    # Rastgele kordinatta hayvan oluşturur.
    def hayvan_olustur(self, hayvan_sınıfı, sayı, cinsiyet=None):
        for _ in range(sayı):
            konumX = random.randint(0, self.arazi.arazi_En)
            konumY = random.randint(0, self.arazi.arazi_Boy)
            if cinsiyet is not None and hayvan_sınıfı in [Tavuk, Horoz, Avci]:
                hayvan = hayvan_sınıfı(konumX, konumY)
            else:
                hayvan = hayvan_sınıfı(konumX, konumY)
            self.hayvanlar.append(hayvan)

    # Hareket fonksiyonu döngü tekrarı 
    def hareket(self):
        for hayvan in self.hayvanlar:
            hayvan.hareket_et(self.arazi)
            
    # Avlanma fonksiyonu 
    # Başarılı ise True başarısız ise False döner.
    def avlan(self):
        for hayvan in self.hayvanlar:
            if isinstance(hayvan, Kurt):
                hayvan.avla(self.hayvanlar)
            elif isinstance(hayvan, Aslan):
                hayvan.avla(self.hayvanlar)
            elif isinstance(hayvan, Avci):
                hayvan.avla(self.hayvanlar)

    # Konsola 
    def hayvan_sayisini_yazdir(self):
        hayvanlarin_sayisi = {}
        for hayvan in self.hayvanlar:
            tür = hayvan.tür
            if tür not in hayvanlarin_sayisi:
                hayvanlarin_sayisi[tür] = 1
            else:
                hayvanlarin_sayisi[tür] += 1
        print("\n1000 adım sonrasında\nKalan Hayvanların Sayısı:")
        for tür, sayi in hayvanlarin_sayisi.items():
            print(f"{tür}: {sayi}")

# Araziye atama      
arazi = Arazi()
hayvan_olusturucu = HayvanOlusturma(arazi)

# Hayvanları araziye dağıtma
hayvan_olusturucu.hayvan_olustur(Koyun, 15)
hayvan_olusturucu.hayvan_olustur(Koyun, 15)
hayvan_olusturucu.hayvan_olustur(Kurt, 5)
hayvan_olusturucu.hayvan_olustur(Kurt, 5)
hayvan_olusturucu.hayvan_olustur(Inek, 5)
hayvan_olusturucu.hayvan_olustur(Inek, 5)
hayvan_olusturucu.hayvan_olustur(Tavuk, 10)
hayvan_olusturucu.hayvan_olustur(Horoz, 10)
hayvan_olusturucu.hayvan_olustur(Aslan, 4)
hayvan_olusturucu.hayvan_olustur(Aslan, 4)
hayvan_olusturucu.hayvan_olustur(Avci, 1)

# Hareket avlanma ve üreme işlemlerini gerçekleştirme
# Döngü 1000 adım sonra biter.
for i in range(1000):
    hayvan_olusturucu.hareket()
    hayvan_olusturucu.avlan()
    hayvan_olusturucu.ureme_kontrol()
    
# Hayvan sayılarını yazdırma
hayvan_olusturucu.hayvan_sayisini_yazdir()
