
# --------------------------
# This code is autogenerated
data = 0
while data not in [1, 2]:
    data = int(input('Which data set do you want to use? 1 = Test, 2 = Input '))
if data == 1:
    fn = 'test'+str(2)+'.txt'
elif data == 2:
    fn = 'input'+str(2)+'.txt'
f = open(fn, 'r')
raw = [j for j in f.read().splitlines()]
# --------------------------

#%% Parsing the entries

numList = []

for r in raw:
    numList.append([int(j) for j in r.split(' ')])
    
#%% Part 1

difList = []

def difMaker(lst):
    difList = []
    for i in range(0, len(lst) - 1):
        difList.append(lst[i+1] - lst[i])
    return difList

for n in numList:
    lst = []
    difList.append(difMaker(n))
    
def checkInts(difList):
    valValues = [1, 2, 3]
    if not all(abs(num) in valValues for num in difList):
        return False
    
    firstSign = difList[0] > 0
    if not all((num > 0) == firstSign for num in difList):
        return False
    
    return True

countSafe = 0
for dL in difList:
    if checkInts(dL):
        countSafe += 1
        
print('Part 1: The total number of safe reports is: ' + str(countSafe))

#%% Part 2

def checkIntsDamper(lst):
    for j in range(len(lst)):
        adjList = [item for i, item in enumerate(lst) if i != j]
        if checkInts(difMaker(adjList)):
            return True
    return False

countSafe = 0 
for nL in numList:
    if checkIntsDamper(nL):
        countSafe += 1

print('Part 2: The total number of safe lists is: ' + str(countSafe))