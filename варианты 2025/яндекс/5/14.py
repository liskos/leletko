m = []
for x in range(190):
    for y in range(190):
        a = int("w", 36) + x*190 + int("n",36) * 190**2 + int("r", 36) +10 * 190 + y * 190**2 + int("y", 36) * 190**3
        if a % 189==0:
            m.append([y*x, a//189])

print(max(m))