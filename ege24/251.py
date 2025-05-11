s = open('24data/24-251.txt').readline()
mx = 0
last = 0
while True:
    a = s.find('A', last)
    d = s.find('D', last)
    if a == -1 or d == -1:
        break
    if a < d:
        if d < s.find('A', a + 1):
            mx = max(mx, d - a + 1)
        last = a + 1
    else:
        if a < s.find('D', d + 1):
            mx = max(mx, a - d + 1)
        last = d + 1
print(mx)