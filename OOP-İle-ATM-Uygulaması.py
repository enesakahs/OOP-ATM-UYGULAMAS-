#[1] BAKIYE SORGULAMA
#[2] KREDI KART BORC SORGULAMA
#[3] PARA CEKME
#[4] PARA YATIRMA
#[5] CIKIS YAP

class Musteri: #VERİTABANIMIZ GİBİ MUSTERI SINIFI OLUSTURDUK
    def __init__(self,ad,soyad,kartsifre,kartbakiye,kartborc,sonodemetarihi):
        self.ad=ad
        self.soyad=soyad
        self.kartsifre=kartsifre
        self.kartbakiye=kartbakiye
        self.kartborc=kartborc
        self.sonodemetarihi=sonodemetarihi
XHesap=Musteri("ahmet","can",123,5000,2000,"19/11*2023")
YHesap=Musteri("mehmet","cakır",123456,6000,2500,"01/08/2023")
TakılanKart=XHesap #TAKILAN KART MUSTERI SINIFINDAN BILGILERI CEKIYOR NORMALDE DB'den ALMASI GEREK

class ATM:
    def __init__(self,atmad):
        self.atmad=atmad
        self.giriskontrol()
        self.dongu=True

    def giriskontrol(self): #SİFRE BİLGİLERİNİ KONTROL EDİP DOGRUYSA PROGRAMA YÖNLENDİRECEK, HATALIYSA GEREKLI MESAJLARI VERİP CIKIS SAĞLAYACAK BLOK
        hak=2
        for i in range(0,3):
            sifre=int(input("Lütfen Kart Sifrenizi Giriniz: "))
            if sifre==TakılanKart.kartsifre:
                self.program()
            elif TakılanKart.kartsifre!=sifre and hak!=0: #SİFRESİ YANLIS VE DENEME HAKKI DEVAM EDIYOR
                print("Sifrenizi Hatalı Girdiniz. Lütfen Kontrol Ediniz. Kalan Hakkınız {}".format(hak))
                hak-=1
            elif TakılanKart.kartsifre!=sifre and hak==0: #SİFRESİ YANLIS VE DENEME HAKKI BİTTİ
                print("Sifrenizi 3 defa yanlış girdiniz. Kartınız Bloke Edildi. En Yakın Subeye Basvurunuz.")
            exit()
    
    def menu(self): #MENU
        secim=int(input("Merhabalar {} {}, {}'a Hosgeldiniz.\n\nLütfen yapmak isteginiz islemi seciniz.\n\n[1] BAKIYE SORGULAMA\n[2] KREDI KART BORC SORGULAMA\n[3] PARA CEKME\n[4] PARA YATIRMA\n[5] CIKIS YAP\n".format(TakılanKart.ad,TakılanKart.soyad,self.atmad)))
        while secim<1 or secim>5:
            print("\n\nLütfen 1 ile 5 arasında gecerli bir deger giriniz.\nAna menüye dönülüyor")
            self.program()#anamenü
        return secim


    def program(self): #görevi menüden bilgi cekmek
        secim=self.menu()

        if secim==1:
            self.bakiyesorgu()
        if secim==2:
            self.kkborc()
        if secim ==3:
            self.paracek()
        if secim==4:
            self.parayatır()
        if secim==5:
            self.cıkısyap()
       
    def bakiyesorgu(self):
        print("Hesabınızda Bulunan Bakiye {} 'TL dir.".format(TakılanKart.kartbakiye))
        self.dongu=False #döngüyü durdurmazsak bizi tekrar  menu secımıne götürür
        self.menuyegeridon


    def kkborc(self):
        print("Kredı kartı borcunuz {} son ödeme tarihli {} 'TL dir.".format(TakılanKart.sonodemetarihi,TakılanKart.kartborc))
        self.dongu=False
        self.menuyegeridon

    def paracek(self):
        cekilecektutar=int(input("Lütfen Cekmek İstediğiniz Tutarı Giriniz: "))
        if cekilecektutar > TakılanKart.kartbakiye:
            print("YETERSIZ BAKIYE")
            self.menuyegeridon()
        else:
            yenibakiye=TakılanKart.kartbakiye - cekilecektutar
            print("para cekme ıslemınız gerceklestı.\nGüncel bakıyenız {} 'TL dir.".format(yenibakiye))
            self.menuyegeridon()

    def parayatır(self):
        yatırılacaktutar=int(input("Yatırmak İstediğiniz Tutarı Giriniz: "))
        yenibakiye_2=yatırılacaktutar + TakılanKart.kartbakiye
        print("para yatırma ıslemınız gerceklestı.\nGüncel bakıyenız {} 'TL dir.".format(yenibakiye_2))
        self.menuyegeridon()

    def cıkısyap(self):
        print("Tesekkurler, İyi günler dileriz.")
        self.dongu=False
        exit()

    def menuyegeridon(self):
        x=int(input("Ana menuye donmek ıcın 7, Kart ıade ıslemı ıcın 5 e basınız."))
        if x==7:
            self.program()
        elif x==5:
            self.cıkısyap()
        else:
            print("Ana menuye donmek ıcın 7, Kart ıade ıslemı ıcın 5 e basınız.")
        return x

banka=ATM("X BANK") #burda ismi biz belirledik
while banka.dongu:  #sistemin sürekli calısır halde olabilmesi icin while dögüsüne
    banka.program() #program blogunu sürekli çalıstır.
            
            
