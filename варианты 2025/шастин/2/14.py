d = 0
for i in range(1, 24):
    a = int("12" + str(i) + "734", 24)
    b = int("8" + str(i) + "95" + str(i) + "3", 24)
    c = int("24" + str(i) + "796", 24)
    if (a + b + c) % 23 == 0:
        d = (a + b + c) // 23
        print((a + b + c) // 23)
