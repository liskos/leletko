s = open("24.txt").read()
s = s.replace("*", "-")
s = s.replace("9", "6").replace("8", "6").replace("7", "6")
s = s.replace("--", "- -").replace("--", "- -")
s = s.replace("-0", " ")
while " 0" in s:
     s = s.replace(" 0", " ")
s = s.replace(" -", " ")
s = s.replace("- ", " ")
m = max([len(x) for x in s.split()])
print(m)
