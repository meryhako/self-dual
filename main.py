import re
import math

def GetAllNums(x):
    temp = re.findall(r'\d+', x)
    res = list(map(int, temp))
    return res

def CreateDict(n, x, InReverse):
    Powed = math.pow(2, n)
    output = {}
    seperate = 2
    AddChar = "1" if InReverse else "0"

    for i in x:
        output["x{0}".format(i)] = ""
        Seped = Powed/seperate
        for j in range(seperate):
            output["x{0}".format(i)] += AddChar*int(Seped)
            AddChar = "0" if AddChar == "1" else "1"
        AddChar = "0"
        seperate *= 2
    
    return output

#konyukcia
def AND(x, y):
    newStr = ""

    for i in range(len(x)):
        newStr += "1" if x[i] == "1" and y[i] == "1" else "0"
    return newStr

def XOR(x, y):
    newStr = ""

    for i in range(len(x)):
        newStr += "0" if x[i] == y[i] else "1"
    return newStr

def SelfDual(x):
    for i in range(round(len(x)/2)):
        if x[i] == x[0-i-1]:
            return False
    return True





# InputData = input('Input your polinom of Jegalkin: ').lower()
InputData = "x1+x2x3+1"

InReverse = False
if InputData.startswith("1+"):
    InReverse = False if InReverse else True
    InputData = InputData[2:]

if InputData.endswith("+1"):
    InReverse = False if InReverse else True
    InputData = InputData[:-2]

if "+1+" in InputData:
    InReverse = False if InReverse else True
    InputData = InputData.replace("+1+", "+")

ListOfID = sorted(list(set(GetAllNums(InputData))))

Trust = CreateDict(len(ListOfID), ListOfID, InReverse)

SplitedIDs = InputData.split("+")

for i in SplitedIDs:
    if i.count('x') > 1:
        itemsInAnd = sorted(list(set(GetAllNums(i))))
        NewTrust = Trust["x{0}".format(itemsInAnd[0])]
        for j in range(1, len(itemsInAnd)):
            NewTrust = AND(NewTrust, Trust["x{0}".format(itemsInAnd[j])])
        Trust[i] = NewTrust

NewTrust = Trust[SplitedIDs[0]]
for i in range(1, len(SplitedIDs)):
    NewTrust = XOR(NewTrust, Trust[SplitedIDs[i]])

print(NewTrust)
print("Is self dual" if SelfDual(NewTrust) else "Is not self dual")
