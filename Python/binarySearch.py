## Created by Sai Chamarty

## This file contains an implementation of binary search.

# Question: 
# You are given n sticks, each having a positive integer length, and you are also given a positive integer k.
# What is the largest length x, such that by cutting sticks as described above, it is possible to obtain 
# at least k sticks, each having length x?


# stickList = input("Please enter the stick lengths with spaces: ")
stickList = "4 5 3 6 7 19"
stickLenghts = [int(x) for x in stickList.split()] # create a list, and covert it into a list of ints
print(stickLenghts)

# sort the list:
stickLenghts.sort()
print(stickLenghts)
low, high = 1, max(stickLenghts)

def binarySearch(lengthsList, k, high, low):
    if low > high:
        return high
    numberOfSticks = 0
    mid = (high + low) // 2
    for i in lengthsList:
        numberOfSticks += (i//mid)
    if numberOfSticks >= k:
        # we can try a higher mid.
        return binarySearch(lengthsList, k, high, mid+1)
    if numberOfSticks < k:
        # we need a lower mid
        return binarySearch(lengthsList, k, mid-1, low)

print(binarySearch(stickLenghts, 3, high, low))