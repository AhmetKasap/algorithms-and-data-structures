
# ! a^b yi hesaplayan algoritma 

a = int(input ("a sayısını giriniz : "))
b = int(input("b sayısını giriniz : "))

sonuc = 1 
for i in range (0,b):
    sonuc = sonuc * a
print(sonuc)
    