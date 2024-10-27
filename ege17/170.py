a = [int(x) for x in open("17data/17-4.txt")]
b = [x for x in a if x % 13 == 4 and x % 8 == 1]
print(max(b), sum(b))