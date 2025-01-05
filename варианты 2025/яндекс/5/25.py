def delit(n):
    a = set()
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n //i)
    return a


k = 0
for i in range(700000+1, 10**10):
    a = delit(i)
    if len(set(a)) == 2 and max(a) - min(a) <= 15:
        k +=1
        print(i,max(a)- min(a), sep="\t")
        if k ==6:
            break