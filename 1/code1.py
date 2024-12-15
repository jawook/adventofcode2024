
# --------------------------
# This code is autogenerated
data = 0
while data not in [1, 2]:
    data = int(input('Which data set do you want to use? 1 = Test, 2 = Input '))
if data == 1:
    fn = 'test'+str(1)+'.txt'
elif data == 2:
    fn = 'input'+str(1)+'.txt'
f = open(fn, 'r')
raw = [j for j in f.read().splitlines()]
# --------------------------

#%% part 1

spltLists = [[],[]]
for r in raw:
    splt = r.split('   ')
    spltLists[0].append(int(splt[0]))
    spltLists[1].append(int(splt[1]))

for lst in spltLists:
    lst = lst.sort()

count = 0
    
for j in zip(spltLists[0], spltLists[1]):
    count += abs(j[0] - j[1])
    
print("The answer for part 1 is {}".format(count))

#%% part 2

simScore = 0

for j in spltLists[0]:
    simScore += j * spltLists[1].count(j)
    
print("The answer for part 2 is {}".format(simScore))