s = open("24data/k7c-3.txt").read()
l = 0
p = 3
r =[]
while p < len(s):
    ws = s[l:p]
    if ws[1] in "BDE" and (ws[2] in "ACD" and ws[2] != ws[1]) and ws[0] == ws[2]:
        r.append(ws)
    l += 1
    p += 1
print(len(r))