s = open("24.txt").read()
for i in range(1,10):
    s = s.replace(f"{i}", "1")

s = s.replace("+", "*").replace("**", " ").replace(" *", " ").replace(" 01", " ")
s = s.replace("00", " ")
r = ""
m = 0
s = s.split()
for i in s:
    if len(i) > m:
        r = i
        m = len(i)

print(r)
print(m)



