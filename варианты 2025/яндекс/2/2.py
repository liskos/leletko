for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            for d in 0, 1:
                f = (not a or b) and (not b or c) and (not c or d)
                print(a, b, c, d, "!", int(f))