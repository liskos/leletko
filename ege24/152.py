f = open("24data/24-j9.txt")
s = f.readline()

k = 0
n = len(s)
for i in range(n):
    if s[i] == s[n-i-1]:
        k += 1
print(k//2)