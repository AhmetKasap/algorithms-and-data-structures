
# !  -------------------------Değişken Tanımlama--------------------------

sayi1 = 15.5 
print(type(sayi1))  # sayi1 tipini öğren (float)
print(int(sayi1))   # tip dönüşümü


mesaj = input("mesajınızı giriniz : ")
sayi = int(input("bir sayı giriniz :"))


# ! ---------------------------- İF - ELSE -----------------------

notunuz= int(input("notunuzu giriniz : "))

if notunuz >= 85 :
    print("Takdir Belgesi İle Geçtiniz")
elif notunuz >= 70 :
    print("Teşekkür Belgesi ile Geçtiniz")
elif notunuz >= 50 :
    print("Belgesiz Geçtiniz")
else:
    print("Sınıfta Kaldınız")


# ! ------------------------------ FOR - WHİLE --------------------------

for i in range (1,10) :              # 1 den başla 10 a kadar git 
    print("Ahmet")                   

for i in range (3,25,+2):            # 3 den başla 2 şer 2 şer artarak 25 e kadar git.
    print(i)

sayi = 0 
while (sayi < 10) :
    print("Merhaba")
    sayi = sayi + 1


# ! ------------------------------String------------------------------------

isim = "Benim adım ahmet"

print(len(isim))   # isim değişkeninin eleman sayısını öğren
print(isim[0])     # isim değişkeninin 0. indisindeki elemanı ekrana yaz. 

# ? String metotları
print(mesaj.upper())  # Çıktı = mesaj içindeki metni komple büyük yazar.
print(mesaj.title())


# ! ---------------------------- Liste -------------------------------------
# * Listelerin en önemli 5 özelliği; ekle - sil - güncelle - ara - yazdır

isimler = ["merhaba","benim","adım","mustafa"]

print(len(isimler))  # dizi boyutu öğrenme
print(isimler[2])    # 2.indis deki elemanı getir

isimler[0] = "Ahmet"  # 0.indis içeriğini güncelle.

for i in range(1, 4):  # listeyi ekrana yazdırma
    print(isimler[i])

for i in isimler :
    print(isimler[i])

# ? liste metotları     

numaralar = [1,7,2,13,39,43,21]
numaralar2 = [10,20,30,40]

print(min(numaralar))   # listenin en küçük elemanını verir.
print(max(numaralar))   # listenin en büyük elemanını verir.

numaralar.append(100)  # direk ekleme
numaralar.insert(5,99)   # indise göre ekeleme

numaralar.remove(7)      # direk silme
numaralar.pop(2)         # indise göre silme
numaralar.clear()       # listedeki tüm elemanları siler

numaralar.index(13)          # 13 sayısını arar ve index değerini döndürür

kopya_numaralar = numaralar.copy()        # listenin bir kopyasını alır

numaralar.sort()        # listeyi sıralar

numaralar.extend(numaralar2) # iki listeyi birleştirme
 


# ! ------------------------------ Fonksiyonlar ------------------------

def toplam (sayi1 , sayi2) :
    sonuc = sayi1 + sayi2
    return sonuc

x = int(input("Bir sayı giriniz : "))
y = int(input("Bir sayı giriniz : "))
k = toplam(x,y)
print(k)



















