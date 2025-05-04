s = open("24data/24-j4.txt").read()
print(s.count("BOSS")- (s.count("BOSSJ")+s.count("JBOSS")) + s.count("JBOSSJ"))
