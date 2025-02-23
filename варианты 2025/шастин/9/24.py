s = open("24.txt").read()
print(s[:100])
s = s.replace("--", "  ").replace("**", "  ")
s = s.replace("-*", "  ").replace("*-", "  ")
s = s.replace(" 0", "  ").replace(" -", "  ")
s = s.replace(" *", "  ").replace("- ", "  ").replace("* ", "  ")
s = s.replace("-0", "  ").replace("*0", "  ")
s = s.split()
r = []
for i in s:
    if i[0] not in "-0*" and i[-1] not in "-*":
        r.append(1+i.count("0") + i.count("6") + i.count("7") + i.count("8") + i.count("9"))




print(sum(r))