
# ! Girilen sayının faktöriyelini hesaplayan algoritma


sayi = int(input("bir sayı giriniz :"))

sonuc = 1
for i in range (1, sayi+1):
    sonuc = sonuc * i 
print(sonuc)