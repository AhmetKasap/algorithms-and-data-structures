'''
num1 = [0,1,2,3,4]
num2 = [5,6,7,8]
x = len(num1)
y = len(num2)
z = x+y
num3 = [0] * (z)

for i in range(0,x):
    num3[i] = num1[i]

for i in range(0,y):
    num3[x+i] = num2[i]

print(num3)

'''

def birlestir (num1,num2):
    x = len(num1)
    y = len(num2)
    z = x+y
    num3 = [0] * (z)

    for i in range(0,x):
        num3[i] = num1[i]

    for i in range(0,y):
        num3[x+i] = num2[i]

    return num3


sonuc = birlestir([0,1,2,3,4],[5,6,7,8,9])
print(sonuc)

