a = [int(x) for x in open("17data/17-288.txt")]
c = []
for i in range(len(a)- 3):
    if abs(a[i]) % 10 == 3 or abs(a[i+1]) % 10 == 3 or abs(a[i+2] % 10 == 3) or abs(a[i+3]) % 10 == 3:
        if abs(a[i]) % 7 != 3 and abs(a[i+1]) % 7 != 3 and abs(a[i+2]) % 7 != 3 and abs(a[i+3]) % 7 != 3:
            c.append(max(a[i:i+4]) - min(a[i:i+4]))
print(len(c), min(c))