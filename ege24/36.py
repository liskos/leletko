s = open("24data/k7c-4.txt").read()
l = 0
p = 3
r =[]
while p < len(s):
    ws = s[l:p]
    if ws[2] in "CDF" and ws[0] in "ADF" and ws[0] != ws[2] and ws[1] in "CDF" and ws[1] != ws[2]:
        r.append(ws)
    l += 1
    p += 1
print(len(r))