# s = open("24.txt").read()
# f1 = open("24_2.txt", mode="w")
m = 10**10
# print("00", file=f1, end="")
# for i in range(2, len(s)-2):
#     if s[i-2] == s[i] and s[i-1] == s[i+1] and s[i] == s[i+2]:
#         print("1", file=f1, end="")
#     else:
#         print("0", file=f1, end="")
# print("00", file=f1, end="")
# f1.close()
f1 = open("24_2.txt")
s = f1.readline()
print(s.count("1"))
a = []
for i in range(len(s)):
    if s[i] == "1":
        a.append(i)
print(a)
for i in range(len(a)-169):
    m = min(a[i+169] - a[i] + 1 + 4, m)
print(m)