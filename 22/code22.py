
# --------------------------
# This code is autogenerated
data = 0
while data not in [1, 2]:
    data = int(input('Which data set do you want to use? 1 = Test, 2 = Input '))
if data == 1:
    fn = 'test'+str(22)+'.txt'
elif data == 2:
    fn = 'input'+str(22)+'.txt'
f = open(fn, 'r')
raw = [j for j in f.read().splitlines()]
# --------------------------
    