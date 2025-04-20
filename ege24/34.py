s = open("24data/k7c-2.txt").read()
l = 0
p = 3
r =[]
while p < len(s):
    ws = s[l:p]
    if ws[0] in "ACE" and (ws[1] in "ADF" and ws[1] != ws[0]) and (ws[2] in "ABF" and ws[2] != ws[1]):
        r.append(ws)
    l += 1
    p += 1
print(len(r))