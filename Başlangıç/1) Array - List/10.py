'''
num1 = [5,10,15,30]

top = 0
for i in range (0,len(num1)):
    top = num1[i] + top

print("Dizinin ortalaması : ", top / len(num1))
'''


def ort(num1):
    top = 0
    for i in range (0,len(num1)):
        top = num1[i] + top
    print("Dizinin ortalaması : ", top / len(num1))

ort([10,20,30])