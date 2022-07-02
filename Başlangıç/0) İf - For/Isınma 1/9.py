
# ! Girilen bir sayının asal olup olmadığını bulan algoritma

sayi = int(input("bir sayı giriniz : "))

for i in range(2, sayi) : 
    if (sayi % i) == 0 :
        print(sayi, "sayısı asal değildir") 
        break
else:
    print(sayi, "sayısı asaldır.")
        
