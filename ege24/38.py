s = open("24data/k7c-6.txt").read()
l = 0
p = 3
r =[]
while p < len(s):
    ws = s[l:p]
    if ws[0] != ws[1] and ws[1] != ws[2] and ws[2] != ws[0]:
        r.append(ws)
    l += 1
    p += 1
print(len(r))