def simpleDividers(n):
   answer = []
   d = 2
   while d * d <= n:
       if n % d == 0:
           answer.append(d)
           n //= d
       else:
           d += 1
   if n > 1:
       answer.append(n)
   return answer

k = 0
for i in range(456789,10**10):
    if k ==5:
        break
    pd = set(simpleDividers(i))
    pd = [x for x in pd]
    if len(pd) < 4:
        m = 0
    else:
        m = pd[0] + pd[1] + pd[-1] + pd[-2]
    if m % 114 == 39:
        print(i,m)
        k += 1