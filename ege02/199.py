for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f =  ( x and ( y or not z )  and w ) == ( not x or not y and z )
                print(x, y, z, w, "!", int(f))