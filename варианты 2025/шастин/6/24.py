s = open("24.txt").read()
while "--" in s:
    s = s.replace("--", "-")

for s1 in s.split():
    print(s[:20])