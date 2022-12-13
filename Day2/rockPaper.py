import pandas as pd

#reading in file and separating for each elf
# filename='test.txt'
filename='input.txt'

elf1=[]
elf2=[]
scores=[]
for line in open(filename):
    listWords = line.strip().split(" ")
    # print(listWords)
    elf1.append(listWords[0])
    elf2.append(listWords[1])   

#putting info into a pandas dataframe
elfScores=pd.DataFrame(data=elf1, columns=['elf'])
elfScores['you']=elf2

#copy for part 2
elfScores2=elfScores.copy()

##### PART 1 #####
#giving a score to each entry
def score(x):
    if x=='A' or x=="X":
        rScore=1
    if x=='B' or x=="Y":
        rScore=2
    if x=='C' or x=="Z":
        rScore=3
    return rScore

elfScores['elfRS']=elfScores['elf'].apply(lambda x: score(x))
elfScores['youRS']=elfScores['you'].apply(lambda x: score(x))

# outcome score..who won
#1 for Rock, 2 for Paper, and 3 for Scissors
# Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock.

def outcome(x):
    if x['youRS']==x['elfRS']:
        outScore=3
        return outScore
    if (x['youRS']==1) & (x['elfRS']==3):
        outScore=6
        return outScore
    if (x['youRS']==2) & (x['elfRS']==1):
        outScore=6
        return outScore
    if (x['youRS']==3) & (x['elfRS']==2):
        outScore=6
        return outScore
    else:
        outScore=0
        return outScore


elfScores['youOutS']=elfScores.apply(outcome, axis=1)
#adding up the score
elfScores['totalYou']=elfScores['youRS']+elfScores['youOutS']
#Result
print(sum(elfScores.totalYou))




##### PART 2 #####

#X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
# x=0
# y=3
# z=6
d={
    'A':1,
    'B':2,
    'C':3,
    'X':0,
    'Y':3,
    'Z':6
}

#elf's score
elfScores2['elfRS']=elfScores2['elf'].apply(lambda x: d.get(x))
# the score you need to get
elfScores2['youStrat']=elfScores2['you'].apply(lambda x: d.get(x))

def strategy(x):
    if x['you']=="Y":
        return x['elf']
    if x['you']=="X":
        if x['elf']=="A":
            return "C"
        if x['elf']=="B":
            return "A"
        if x['elf']=="C":
            return "B"
    else:
        if x['elf']=="A":
            return "B"
        if x['elf']=="B":
            return "C"
        if x['elf']=="C":
            return "A"

# getting what move you need to do
elfScores2['youPlay']=elfScores2.apply(strategy, axis=1)
# your round score
elfScores2['youRS']=elfScores2['youPlay'].apply(lambda x: d.get(x))
# your out score
elfScores2['youOutS']=elfScores2.apply(outcome, axis=1)
# outcome score
elfScores2['totalYou']=elfScores2['youRS']+elfScores2['youOutS']

#Result for part 2
print(sum(elfScores2.totalYou))