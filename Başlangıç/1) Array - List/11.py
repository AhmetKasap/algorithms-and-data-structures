num = [19,200,3,40,110]

for j in range (0, len(num)):
    for i in range (0,len(num)):
        if num[i] < num [i+1]:
            print("min : ", num[i])
            break
    break