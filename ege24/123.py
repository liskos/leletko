s = open("24data/24-1.txt").read()
maxim = 0
r = []
counter = 0
for i in range(1, len(s)-1):
    if s[i] > s[i-1] and s[i] > s[i+1]:
        counter += 1
        r.append(i)
    else:
        counter = 0
    if counter > maxim:
        maxim = counter
        
g = []
for i in range(len(r)-1):
    g.append(r[i+1]-r[i])
print(maxim)
print(max(g))