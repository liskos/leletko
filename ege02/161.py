for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
             f =  ( x or not y or not z) and ( x or y or not z) and ( z or y or z)
             print(x, y, z,  "!", int(f))