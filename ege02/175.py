for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            f =  not ( z or y ) or ( x == z )
            print(x, y, z,  "!", int(f))