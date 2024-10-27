for a in range(1, 100):
    if all(x&57 == 0 or ( not(x&23 == 0 ) or (not(x&a == 0))) for x in range(1,1000)):
        print(a)
        break