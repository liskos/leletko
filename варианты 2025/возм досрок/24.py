s = open("24.txt").read()
a = "3579"
for i in a:
    s =s.replace(f"{i}", "1")
print(s[:100])
s = s.replace("+", "*").replace("**", " ").replace("1*", " ").replace("*0", " ")
print(s[:100])
s = s.split()
r = []
for i in s:
    r.append(len(i))

print(max(r))