a = [int(x) for x in open("17data/17-4.txt")]
b = [x for x in a if x % 13 == 7 and x % 7 != 0 and x % 11 != 0]
print(max(b) - min(b), len(b))