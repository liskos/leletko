s = open("24.txt").read()
s = s.replace("4", "a").replace("3", "e")
t = "yandex"
while t in s:
    t += "yandex"
print(t)
print(t in s)
t = t[:-1]
print(t)
print(t in s)
t = t[:-1]
print(t)
print(t in s)
t = t[:-1]
print(t)
print(t in s)
t = t[:-1]
print(t)
print(t in s)
t = t[:-1]
print(t)
print(t in s)
t = t[:-1]
print(t)
print(t in s)
print(len(t))