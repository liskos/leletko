s = open("24.txt").read()
ind = [i for i in range(len(s)) if s[i:i+4] == "UPIT"]
k = 80 # 80
m = 0
for i in range(0, len(ind)-(k-1)):
    if i - 1 < 0:
        i1 = 0
    else:
        i1 = ind[i-1] + 1
    if i + k == len(ind):
        i2 = len(s)-1
    else:
        i2 = ind[i+k] + 2
    m = max(m, i2-i1 + 1)
print(m)

