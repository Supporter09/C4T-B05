name = ["ST","BĐ","BTL","CG","ĐĐ","HBT"]
population = [150300,247100,333300,266800,420900,318000]
km2 = [117.43,9.224,43.35,12.04,9.96,10.09]
MDDC =[]
totalpop = 0

for i,pop in enumerate(population):
    MDDC.append(km2[i]/pop)
for m in MDDC:
    totalpop += m

totalname = len(name)
print(totalname)

MDDCTB = totalpop/totalname
print(MDDCTB)
