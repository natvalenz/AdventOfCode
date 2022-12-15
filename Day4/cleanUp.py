##### PART 1 ####

## using set and is subset or all
# filename='test.txt'
filename='input.txt'
reconsider=0
for string in open(filename):
    string=string.strip('\n')
    stringList=string.split(',')
    firstpart, secondpart=list(map(int,stringList[0].split('-'))),list(map(int,stringList[1].split('-')))
    firstElf=[x for x in range(firstpart[0], firstpart[1]+1)]
    secondElf=[x for x in range(secondpart[0], secondpart[1]+1)]

#     if all(item in firstElf for item in secondElf) or all(item in secondElf for item in firstElf):
    if set(firstElf).issubset(secondElf) or set(secondElf).issubset(firstElf):
        reconsider+=1
        
print(reconsider)

## using operators
# filename='test.txt'
filename='input.txt'
reconsider=0
for string in open(filename):
    string=string.strip('\n')
    stringList=string.split(',')
    firstpart, secondpart=list(map(int,stringList[0].split('-'))),list(map(int,stringList[1].split('-')))
    firstElfA, firstElfB = firstpart[0], firstpart[1]
    secondElfA, secondElfB =secondpart[0], secondpart[1]
    if (firstElfA <= secondElfA and firstElfB >= secondElfB ) or (secondElfA<=firstElfA and secondElfB>=firstElfB):
        reconsider+=1
        
print(reconsider)


##### PART 2 #####
## using any
# filename='test.txt'
filename='input.txt'
reconsider=0
for string in open(filename):
    string=string.strip('\n')
    stringList=string.split(',')
    firstpart, secondpart=list(map(int,stringList[0].split('-'))),list(map(int,stringList[1].split('-')))
    firstElf=[x for x in range(firstpart[0], firstpart[1]+1)]
    secondElf=[x for x in range(secondpart[0], secondpart[1]+1)]

    if any(item in firstElf for item in secondElf) or any(item in secondElf for item in firstElf):
#     if set(firstElf).issubset(secondElf) or set(secondElf).issubset(firstElf):
        reconsider+=1
        
print(reconsider)


## using operators
# filename='test.txt'
filename='input.txt'
reconsider=0
for string in open(filename):
    string=string.strip('\n')
    stringList=string.split(',')
    firstpart, secondpart=list(map(int,stringList[0].split('-'))),list(map(int,stringList[1].split('-')))
    firstElfA, firstElfB = firstpart[0], firstpart[1]
    secondElfA, secondElfB =secondpart[0], secondpart[1]
    if (firstElfA <= secondElfA <= firstElfB ) or (secondElfA <=firstElfA <=secondElfB):
        reconsider+=1
        
print(reconsider)