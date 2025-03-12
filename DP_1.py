# using bellman equation to solve the coin changing problem.

denominations = [3, 5, 7]
n = 18
OPT = [float('inf')]*(n+1)
print(OPT)
OPT[0] = 0

for i in range(1, n+1): # for each n
    for c in denominations: # try each denomination
        if i - c >=0 and OPT[i - c] != float('inf'):
            OPT[i] = min(OPT[i], 1 + OPT[i - c])

for i in range(n + 1):
    if OPT[i] == float('inf'):
        OPT[i] = -1

print(OPT)

