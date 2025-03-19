# Data-Structures-and-Algorithms
This repository consists of all the data structures and algorithms I learned and their example implementations.

# Binary Search Algorithm
This algorithm is used to efficiently look up a particular item, for example a number, from an array which is sorted in ascending or descending order.

## Time Complexity: O(log n)
n is the length of the array being searched

## Pseudocode:
sortedArray = [...]
requiredNum = x
indexInArray = -1 # to be calculated if it exists

low = 0
high = len(sortedArray) - 1

while low <= high:
    mid = (low + high)/2
    if sortedArray[mid] > requiredNum:
        high = mid-1
    else if sortedArray[mid] < requriedNum:
        low = mid+1
    else:
        index = mid
        break