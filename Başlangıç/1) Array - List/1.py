sayilar = [10,7,13,21,14]
x = len(sayilar)

aranan = int(input("Diziden aramak istediğiniz elemanı giriniz : "))

for i in sayilar:
    if (aranan == i) :
        print("aranan sayi: ", i)    
    else:
        False
        
for i in range(1,x) :
    if (sayilar[i]) == (aranan) :
        print("aranan sayinin indexi : " , i)
    else:
        False
        

    
