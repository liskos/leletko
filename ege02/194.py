for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f =  (( x and w ) or ( w and z )) == (( not z or y ) and ( not y or x ))
                print(x, y, z, w, "!", int(f))