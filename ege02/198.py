for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f =  ( not w or y ) and (( not x or z ) == ( not y or x ))
                print(x, y, z, w, "!", int(f))