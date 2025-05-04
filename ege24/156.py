s=open('24data/24-153.txt').read()
k=0
for i in range(len(s)-3):
    if s[i] == "A" and s[i+6:i+10].count("F") >0:
        k += s[i+6:i+10].count("F")
print(k)