for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f =  not ( not x or w ) or ( not y or z ) or ( not y )
                print(x, y, z, w, "!", int(f))