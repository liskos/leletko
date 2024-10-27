a = [int(x) for x in open("17data/17-4.txt")]
b = [x for x in a if (x % 10 + x % 100 // 10 >= 15) and x % 3 != 0 and x % 4 != 0 and x % 7 != 0]
print(min(b), sum(b))