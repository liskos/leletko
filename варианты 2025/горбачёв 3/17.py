a = [int(x) for x in open("17.txt")]
r = []
for i in range(len(a)-2):
    k = 0
    if a[i] % 11 == 0 and str(a[i])[-1] == "3":
        k = k +1
    if a[i+1] % 11 == 0 and str(a[i+1])[-1] == "3":
        k = k +1
    if a[i+2] % 11 == 0 and str(a[i+2])[-1] == "3":
        k = k +1
    if k == 2:
        r.append((a[i]+a[i+1]+a[i+2])*2)

print(len(r), min(r))
