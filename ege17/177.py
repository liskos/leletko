a = [int(x) for x in open("17data/17-4.txt")]
b = [x for x in a if str(x).count("0") >= 2 and x % 7 == 0]
print(len(b), max(b))