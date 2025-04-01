# Here we will implement the famous knapsack problem to get a better understanding of Dynamic Programming.

# Problem Statement:
'''
You have a knapsack with a maximum weight capacity of 15 units. There are 4 items available, each with
its own weight and value:
Item 1. Weight = 5, Value = 10
Item 2: Weight = 4, Value = 40
Item 3: Weight = 6, Value = 30
Item 4: Weight = 3, Value = 50

Your task:
Determine the maximum total value you can pack into the knapsack without exceeding its weight capacity.
Also, identify which items make up this optimal solution

HINT:
1. Define the Subproblem:
    Let OPT(i, w) be the maximum value achievable with the first i items and a knapsack capacity of w.

2. Recurrence Relation:
    For each item i (with weights w_i and value v_i) and capacity w:
    Case 1: Do not include item i:
    OPT(i, w) = OPT(i - 1, w)

    Case 2: Include item i (if w_i <= w):
    OPT(i, w) = v_i + OPT(i - 1, w - w_i)

    Then choose the maximum of these two cases

3. Build a DP_table
    Create a dp table with rows representing the tiems (from 0 to 4) and columns representing
    capacities from 0 to 15. Fill the table using the reccurrence relation above.

4. Traceback:
    After filling the table, trace back through it to identify which items were included in the optimal solution.

    How does traceback work?

    1. Start at the End:
        Begin at cell dp[n][W], where n is the number of items and W is the total capacity.
    2. Compare current and previous rows:
        For each item i (starting from n and moving backwards) and the current capacity w

        - if dp[i][w] == dp[i-1][w]:
            This means that the item i was not included in the optimal solution, so you move to the next item
            i - 1 without changing the capacity w.
        - if dp[i][w] != dp[i - 1][w]:
            This indicated that item i was included in the optimal solution. You record item i as part of the 
            solution, and then update the capacity by subtracting the weight of that item:
            w = w - input_items[i][weight]

        Then move to item i-1.
    3. Termination:
        The traceback process stops when you have processed all items (i.e., i = 0) or when the remaining 
        capacity w becomes 0.
'''

input = {
    1: {"weight": 5, "value": 10},
    2: {"weight": 4, "value": 40},
    3: {"weight": 6, "value": 30},
    4: {"weight": 3, "value": 50},
}

n = 4 # number of items
W = 15 # weight capacity
dp = [[0] * (W+1) for _ in range(n+1)]



for i in range(1, n+1):
    for w in range(1, W+1):
        # if the current capacity is less than the weight of the item i
        # we cannot include the item
        if w < input[i]["weight"]:
            dp[i][w] = dp[i - 1][w]
        else:
            dp[i][w] = max(
                dp[i - 1][w], # not including the item
                input[i]["value"] + dp[i - 1][w - input[i]["weight"]] # including the item
                )

# We traceback to get the optimal solution
i = n
w = W 
solution = []
optimal_value = 0
while i > 0 and w > 0:
    if dp[i][w] != dp[i - 1][w]:
        # we included this item, so reduce w by its weight
        w = w - input[i]["weight"]
        optimal_value += input[i]["value"]
        solution.append(i)
        i -= 1
    else:
        i -= 1
        continue



print(solution)
print(optimal_value)