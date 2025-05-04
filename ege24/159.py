f = open("24data/24-157.txt")
x = f.read()
count = {}
for i in range(1, len(x) - 1):
	if x[i - 1] == x[i + 1]:
		if x[i] not in count:
			count[x[i]] = 1
		else:
			count[x[i]] += 1

print(count)