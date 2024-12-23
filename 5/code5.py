
# --------------------------
# This code is autogenerated
data = 0
while data not in [1, 2]:
    data = int(input('Which data set do you want to use? 1 = Test, 2 = Input '))
if data == 1:
    fn = 'test'+str(5)+'.txt'
elif data == 2:
    fn = 'input'+str(5)+'.txt'
f = open(fn, 'r')
raw = [j for j in f.read().splitlines()]
# --------------------------

#%% Reshaping list

# locate the divider character
div = raw.index('')

rules = []
for j in raw[:div]:
    rules.append(tuple([int(i) for i in j.split('|')]))
    
orders = []
for j in raw[div+1:]:
    orders.append(tuple([int(i) for i in j.split(',')]))
    
#%% Part 1

def chkOrder(rules, order):
    valid = True
    ruleNum = 0
    while valid and ruleNum < len(rules):
        valid = chkRule(rules[ruleNum], order)
        ruleNum += 1
    return valid
        
def chkRule(rule, order):
    # If both pages of the rule are not in the order, it cannot fail
    if not (rule[0] in order and rule[1] in order):
        return True
    if order.index(rule[0]) < order.index(rule[1]):
        return True
    return False

total = 0
for j in orders:
    if chkOrder(rules, j):
        total += j[len(j)//2]
        # print(j[len(j)//2])
        
print('Part 1: The result is: ' + str(total))

#%% Part 2

# below was found using copilot - need to explore more
from collections import defaultdict, deque

def findOrder(pairs):
    # Create a graph and in-degree dictionary
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    
    # Build the graph and in-degree dictionary from the pairs
    for a, b in pairs:
        graph[a].append(b)
        in_degree[b] += 1
        if a not in in_degree:
            in_degree[a] = 0
    
    # Initialize a queue with nodes that have no incoming edges
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    
    # Perform topological sort
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Check if there was a cycle
    if len(order) != len(in_degree):
        return "There is no valid ordering due to a cycle."
    
    return order

def adjRules(rules, order):
    # Function removes non applicable orders and returns the relevant rule 
    # list
    ordNums = set()
    
    for n in order:
        ordNums.add(n)
        
    revRules = []
    for rule in rules:
        if rule[0] in ordNums and rule[1] in ordNums:
            revRules.append(rule)
            
    return revRules

#%%

order = findOrder(rules)

total = 0
for j in orders:
    if not chkOrder(rules, j):
        revRules = adjRules(rules, j)
        fullOrder = findOrder(revRules)
        total += fullOrder[len(j)//2]
        
print('Part 2: The result is: ' + str(total))