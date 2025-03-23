s = open("24.txt").read()

s = s.replace('-', "*").replace("**", " ").replace(" *", " ").replace("01", "1")
s.replace(" 0", " ").replace("*0"," ").replace("00", " ")
r = ""
m = 0
s = s.split()
for i in s:
    if len(i) > m:
        m = len(i)
        r = i

print(s[:100])
print(m)
print(r)
