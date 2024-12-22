for x in range(25):
    z = "0123456789abcdefghijklmno"
    a = int("a4" + str(z[x]) + "7f2", 25)
    b = int("n" + str(z[x]) + "g5" + str(z[x]) + "h" ,25)
    c = int("74" + str(z[x]) + "m26", 25)
    if (a + b + c) % 24 == 0:
        print((a+b+c) // 24)