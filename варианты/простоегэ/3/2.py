for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f =  not ( not x or ( not ( not w or w ))) and ( not ( not z ) or ((not w) == y))
                print(x, y, z, w, "!", int(f))