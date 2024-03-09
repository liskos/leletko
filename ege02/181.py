for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            f =  ( not y or ( z and x )) or ( x == y)
            print(x, y, z,  "!", int(f))