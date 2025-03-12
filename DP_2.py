# Here we will implement Needleman-Wunsch Algorithm and Bellman equation, for Sequence Alignment of two strings!
# Needleman-Wunsch algorithm uses Dynamic Programming to find minimum cost for aligning the two strings.

s1 = "BABCB"
s2 = "CBBBCC"

# create a 2d array for the dp table
dp_table = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)] 

# let us initialize the dp table with gap_penalities
gap_penality = 2
mismatch_penality = 1

for i in range(1, len(dp_table)):
    dp_table[i][0] = dp_table[i-1][0] + gap_penality

for j in range(1, len(dp_table[0])):
    dp_table[0][j] = dp_table[0][j-1] + gap_penality

# we create a function named match_mismatch to check 
# if the corresponding letter of s1(i) matches with that of s2(j) 
# if yes, we return 0 else we return 1 

def match_mismatch(i, j):
    if s1[i-1] == s2[j-1]:
        return 0
    else:
        return 1

# we implement our Bellman Equation here:
top = 0
left = 0
diagonal = 0

for r in range(1, len(dp_table)):
    for c in range(1, len(dp_table[0])):
        top = dp_table[r-1][c] + gap_penality
        left = dp_table[r][c-1] + gap_penality
        diagonal = dp_table[r-1][c-1] + match_mismatch(r, c)
        dp_table[r][c] = min(top, left, diagonal)


# let us print out the table in a readable form:
for row in dp_table:
    print(" ".join(str(cell) for cell in row))