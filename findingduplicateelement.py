# Find the duplicate element in a limited range array
# Given a limited range array of size n containing
# elements between 1 and n-1 
# with one element repeating, find the duplicate number in it without
# using
#  any extra space.

# For example,

# Input:  { 1, 2, 3, 4, 4 }Output: The duplicate element is 4  
# Input:  { 1, 2, 3, 4, 2 }Output: The duplicate element is 2

def solution(A):
    
    duplicate_value = None
    for i in A:
        if A.count(i) > 1:
            duplicate_value = i
            break #breakout once the firts duplicate is found
    return duplicate_value

    

def solution(A):
    # Phase 1: Finding the intersection point of the two runners.
    slow = A[0]
    fast = A[0]
    
    while True:
        slow = A[slow]
        fast = A[A[fast]]
        if slow == fast:
            break
    
    # Phase 2: Finding the entrance to the cycle.
    slow = A[0]
    while slow != fast:
        slow = A[slow]
        fast = A[fast]
    
    return slow

# Test cases
print(solution([1, 2, 3, 4, 4]))  # Output: 4
print(solution([1, 2, 3, 4, 2]))  # Output: 2


        

   


print(solution({ 1, 2, 3, 4, 4 }))
print(solution({ 1, 2, 3, 4, 2 }))