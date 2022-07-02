
#! Klavyeden girilen bir sayının tam bölenlerinin bulunması

sayi = int(input("bir sayı giriniz : "))


for i in range (1,sayi+1):
    if (sayi % i == 0) :
        print(i)
    