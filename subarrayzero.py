# Check if a subarray with 0 sum exists or not
# Given an integer array, check if it contains a subarray having zero-sum.

# For example,

# Input:  { 3, 4, -7, 3, 1, 3, 1, -4, -2, -2 } Output: Subarray with zero-sum exists
# The subarrays with a sum of 0 are: 
# { 3, 4, -7 }
# { 4, -7, 3 }
# { -7, 3, 1, 3 }
# { 3, 1, -4 }
# { 3, 1, 3, 1, -4, -2, -2 }
# { 3, 4, -7, 3, 1, 3, 1, -4, -2, -2 }
# Note that the problem deals with subarrays that are contiguous,
#  i.e., whose elements occupy consecutive positions in the array.
import random
def solution(A):
    N = len(A)


    # random.shuffle(A) useless for this solution
    '''
    this loops iterates over each element in the array it serves as the starting point for creating subarrays
    for example if A=[3,4,-7,3] the outer loop will run with i=0 (starting at the first element) then i = 1(starting from the second element)
    the inner loop starts from the index i (current starting index) and iterates up to the last element of the array(N)
    current_sum is used to accumulate the sum of the subarray as we iterate through the array from index i to j
    '''
    for i in range(N):
        
        current_sum = 0
        for j in range(i, N):
            '''
        for each j we add the current element A[j] to current_sum. This accumulates the sum of the subarray at index i and ending at index j 
        '''
            current_sum += A[j]
            #check if the current sum is zero
            if current_sum == 0:
                print(f"Subarray with zero-sum exists: {A[i:j+1]}")
                return True
    print("No subarray with zero-sum exists")
    return False
        

    


print(solution([ 3, 4, -7, 3, 1, 3, 1, -4, -2, -2 ]))