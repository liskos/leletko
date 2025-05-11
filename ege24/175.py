s=open("24data/24-175.txt").read()
m=0
d=s.split('KEGE')
for i in range(len(d)-2):
    m=max(m,len(d[i])+len(d[i+1])+len(d[i+2])+4*2)
print(m+6)

