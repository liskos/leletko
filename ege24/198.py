def f(s):
    if len(s) < 3:
        return False
    return (s[0] in "XZ") and (s[2] == "Y")

max_k = 0
s = open("24data/24-197.txt").read()
for l in [i for i in range(len(s)) if f(s[i:i+3])]:
    k = 1
    r = l + 2
    while  f(s[r+1:r+4]):
            r += 3
            k += 1
    if k > max_k:
        max_k = k
        print(k, s[l:r+1])
print(max_k)