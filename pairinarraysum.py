# Find a pair with the given sum in an array
# Given an unsorted integer array, find a pair with the given sum in it.

# For example,

# Input: nums = [8, 7, 2, 5, 3, 1]target = 10 Output: Pair found (8, 2)orPair found (7, 3)  
# Input: nums = [5, 2, 6, 8, 1, 9]target = 12 Output: Pair not found
import random
def solution(A,T):
    N = len(A)
    #shuffle the list into a random order
    random.shuffle(A)
    # print(A)
    '''
    initializa a set called seen. A set is a data structure that stores unique values. We use it to track of the numbers
    we've already encountered while iterating through the list
    '''
    seen = set()
    #begin a loop that will iterate every number in the shuffled list
    for i in A:
        '''
        for each number (i) we calculate the complement, which is the difference between the target sum T and the current number i
        example if i == 7 and T == 10 then the complement would be 10 - 7 = 3
        '''
        complement = T - i
        if complement in seen:
            return f"pair found ({complement}, {i})"
        '''
        if the complement is not found in the set, we add the current number i to the seen set. This allows us to check this number
        aganist future numbers in the array for possible pairs
        
        '''
        seen.add(i)
    return "pair not found"
   

print(solution([8,7,2,5,3,1], 10))
print(solution([5,2,6,8,1,8], 12))