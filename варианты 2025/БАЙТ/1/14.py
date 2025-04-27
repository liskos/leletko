import string
t = "0123456789abcdefghijk"
for x in range(16,len(t)):
    for y in range(len(t)):
        if x > y:
            a = int(f"13f1{t[y]}", x) + int(f"15{t[x]}5{t[y]}", 21)
            if a % 32 == 0:
                print(a//32)