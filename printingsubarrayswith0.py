# Print all subarrays with 0 sum
# Given an integer array, print all subarrays with zero-sum.

# For example,

# Input:  { 4, 2, -3, -1, 0, 4 }
#  Subarrays with zero-sum are { -3, -1, 0, 4 }
# { 0 } 
#  Input:  { 3, 4, -7, 3, 1, 3, 1, -4, -2, -2 } Subarrays with zero-sum are
#  { 3, 4, -7 }{ 4, -7, 3 }{ -7, 3, 1, 3 }{ 3, 1, -4 }{ 3, 1, 3, 1, -4, -2, -2 }
# { 3, 4, -7, 3, 1, 3, 1, -4, -2, -2 }
# Note that the problem deals with subarrays that are contiguous, i.e., 
# whose elements occupy consecutive positions in the array.
def solution(A):
    N = len(A)
   

    for i in range(N):
        current_sum = 0
        for j in range(i, N):
            
            current_sum += A[j]
    return current_sum


print(solution({ 4, 2, -3, -1, 0, 4 }))
# print(solution({ 3, 4, -7, 3, 1, 3, 1, -4, -2, -2 }))