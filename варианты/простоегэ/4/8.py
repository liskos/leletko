a = []
for s1 in "0123456789abcdef":
    for s2 in "0123456789abcdef":
        for s3 in "0123456789abcdef":
            if int(s1, 16) > int(s2, 16) > int(s3, 16):
                a.append(s1+s2+s3)
for s1 in "0123456789abcdef":
    for s2 in "0123456789abcdef":
        for s3 in "0123456789abcdef":
            for s4 in "0123456789abcdef":
                for s5 in "0123456789abcdef":
                    if int(s1, 16) > int(s2, 16) > int(s3, 16)> int(s4, 16) > int(s5, 16):
                        a.append(s1+s2+s3+s4+s5)
print(len(a))