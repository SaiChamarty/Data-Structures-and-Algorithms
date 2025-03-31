# We will learn how greedy algorithms work!
# Greedy algorithms solve optimization problems by making the best local choice at each step in the hope of finding the global optimum. 

#  Example 1: Interval Scheduling

def compatible(i, j):
    if j[0] > i[1] and j[1] > i[0]:
        return True
    else:
        return False

 
def createSchedule(intervals):
    numberOfIntervals = 0
    last_finish = 0 # make sure it is less than intial value of the scheduling
    for start, finish in intervals:
        if start > last_finish:
            numberOfIntervals += 1
            last_finish = finish

    return numberOfIntervals

intervals = [(2,13), (6,15), (12, 16), (14, 21), (12, 12), (18, 20), (12, 16), (8, 9), (9, 13), (6,6)]
intervals.sort(key=lambda x:x[1]) # sorts based on the second value of each tuple in the list
# [(6, 6), (8, 9), (12, 12), (2, 13), (9, 13), (6, 15), (12, 16), (12, 16), (18, 20), (14, 21)]
# print(intervals)
print(createSchedule(intervals))



