s = open("24data/24.txt").read()

t = ""
maxlen = 0
maxstroka = ""
index_prime_sumvola = 0
for i in range(len(s)):
    if t == "":
        t = s[i]
    elif t[-1] < s[i]:
        t += s[i]
    else:
        t = s[i]
    if len(t) > maxlen:
        maxlen = len(t)
        maxstroka = t
        index_prime_sumvola = i - len(t) + 1 + 1
print(maxlen)
print(maxstroka)
print(index_prime_sumvola)