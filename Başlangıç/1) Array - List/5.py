
num = [10,5,7,13]

def sirala(num):
    x = len(num)
    for i in range(0, x-1):
        for j in range(0, x-1) :
            if num[j] > num[j+1]:
                gecici = num[j+1]
                num[j+1] = num[j]
                num[j] = gecici
    print(num)

sirala(num)
