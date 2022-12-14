##### Part 1 #####
# filename='test.txt'
filename='input.txt'
sumPriorities=0
for string in open(filename):
    firstpart, secondpart = set(string[:len(string)//2]), set(string[len(string)//2:])
    for i in firstpart:
        if i in secondpart:
            if i.islower():
                sumPriorities+=(ord(i)-96)
            else:
                sumPriorities+=(ord(i)-38)
print(sumPriorities)

##### Part 2 #####

# filename='test.txt'
filename='input.txt'
sumPriorities=0
elfGroup=[]

for string in open(filename):
    string=string.strip('\n')
    if len(elfGroup)<3:
        elfGroup.append(string)
        if len(elfGroup)==3:
            firstpart, secondpart, thirdpart=set(elfGroup[0]),set(elfGroup[1]),set(elfGroup[2])
            for i in firstpart:
                if i in secondpart and i in thirdpart:
                    if i.islower():
                        sumPriorities+=(ord(i)-96)
                    else:
                        sumPriorities+=(ord(i)-38)
            elfGroup=[]

print(sumPriorities)