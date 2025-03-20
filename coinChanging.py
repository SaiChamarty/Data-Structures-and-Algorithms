# here, we will implement coin changing problem to understand how Dynamic Programming in 1D works.

'''
    Given coin denominations D = {1, 3, 4} and a target value V = 6, use a dynamic programming
    approach to determine:
    1. The minimum number of coins needed to make change for 6.
    2. One optimal set of coins that sums to 6

    HINT:
    Define OPT(v) as the minimum number of coins needed to form the value v, with 
    recurrence:
        OPT(0) = 0, and for v > 0,
        OPT(v) = min {OPT(v-d) + 1} for all coin denominations d such that v-d >= 0.
'''

D = [1, 3, 4]
V = 6
memo = {} # this is for caching purposes. If one v is already computed, then we return that value when called again.

# RECURSIVE IMPLEMENTATION -----------------------------------------------------------------------------------
def OPT(v):
    if v == 0:
        return 0
    
    if v in memo:
        return memo[v]
    
    minCoins = float('inf')

    for coin in D:
        if (v - coin) >= 0:
            # recursively compute the minimum coins needed for (V - coin)
            result = OPT(v - coin)

            if result != float('inf'):
                minCoins = min(minCoins, result + 1)
    
    # Store the computed result in memo for future reference.
    memo[v] = minCoins
    return minCoins

print("Minimum coins needed using recursion:", OPT(V))
# -------------------------------------------------------------------------------------------------------------


# ARRAY IMPLEMENTATION ----------------------------------------------------------------------------------------
OPT_array = [float('inf')]*(V+1)

# Base case:
OPT_array[0] = 0

# Compute the solution for every value from 1 to V
for v in range(1, V+1):
    # Consider each coin denomination
    for coin in D:
        if coin <= v:
            OPT_array[v] = min(OPT_array[v], OPT_array[v - coin] + 1)


print("Minimum coins needed using arrays:", OPT_array[V])
# -------------------------------------------------------------------------------------------------------------
