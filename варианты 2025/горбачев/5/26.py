file = open("26.txt")
n,m,k = map(int,file.readline().split())
print("n ", n, "число занятых мест")
print("m",m, "количество рядов")
print("k",k,"количесво мест в ряду")
a = [m]*(k+1)
for _ in range(n):
    x, y = map(int, file.readline().split())
    a[y] = min (a[y], x)
c = []
for i in range(len(a)-3):
    c.append([min(a[i:i+4]), i+3])
print(c)
m1 = max(c, key=lambda x:x[0])[0]
print(m1-1, "ответ 1")
r = [x for x in c if x[0]==m1]
print(r)