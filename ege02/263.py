for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f =  not ( x or y or z ) or ( x and ( y or w )) 
                print(x, y, z, w, "!", int(f))