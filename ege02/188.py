for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f =  ( w and y ) or (( not x or w ) == ( not y or z ))
                print(x, y, z, w, "!", int(f))