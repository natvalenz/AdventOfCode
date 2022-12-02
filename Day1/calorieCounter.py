with open('input.txt') as f:
    lines = f.readlines()
    lines.append('\n')
    elfSums=[]
    elfCal=0
    for l in lines:
        ele=l
        if ele!="\n":
            ele=int(ele)
            elfCal+=ele
        else:
            elfSums.append(elfCal)
            elfCal=0
    elfSums.sort(reverse = True)
    print("Part 1:",elfSums[0])
    print("Part 2:",sum(elfSums[:3]))