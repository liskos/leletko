for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            f = not  ( not z or not y )  or ( x == z )
            print(x, y, z,  "!", int(f))