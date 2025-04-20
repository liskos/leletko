s = open("24data/k7c-5.txt").read()
l = 0
p = 5
r =[]
while p < len(s):
    ws = s[l:p]
    if ws[0] != ws[1] != ws[2] != ws[3] != ws[4]:
        r.append(ws)
    l += 1
    p += 1
print(len(r))