a = [int(x) for x in open("17data/17-4.txt")]
b = [x for x in a if hex(x)[-1] == "b" and x % 7 == 0 and x%6!=0 and x%13!=0 and x%19!=0]
print(sum(b), len(b))