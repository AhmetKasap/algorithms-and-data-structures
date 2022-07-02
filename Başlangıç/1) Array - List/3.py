sayilar = [10,20,30,40,50,70]
x = len(sayilar)

ekle = int(input("Eklemek istediğiniz elemanı giriniz : "))
guncelle = int(input("Hangi sayı yerine eklemek istediğinizi giriniz : "))


for i in range (0, x, +1):
    if (sayilar[i]) == (guncelle) :
        sayilar[i] = ekle


print("Güncellenmiş Dizi")
for i in sayilar:
    print(i)

print("-------------------------------------------------------------------")

sayilar2 = [10,20,30,40,50,70]
y = len(sayilar2)

def guncelle(ekle,guncelle) :
    for i in range (0, y, +1):
        if (sayilar2[i]) == (guncelle) :
            sayilar2[i] = ekle

guncelle(99999999,50)
print("Güncellenmiş Dizi")
for i in sayilar2:
    print(i)

