k = 0
for i in range(1,int(333396001 ** 0.5)+1):
    if 333396000 % i == 0:
        if i == 333396000 // i:
            k += 1
        else:
            k += 2
print(k)