s = open("24data/k7-m22.txt").read()
l = 0
p = 3
r =[]
while p <= len(s):
    ws = s[l:p]
    rws = sorted(ws)[0] + sorted(ws)[1] + sorted(ws)[2]
    rws = rws[::-1]
    if ws == rws and ws[0] != ws[1] != ws[2]:
        r.append(l)
        print(ws,rws)
    l += 1
    p += 1
print(len(r),r[-1])