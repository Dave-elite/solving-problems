# You are given a string S consisting of N lowercase English letters.
# In how many ways can we split S into two non-empty parts, such that in at least one part the letter 'x' and the letter 'y'
# occur the same number of times?
# Write a function:
# function solution(S);
# that, given a string S of length N, returns the number of splits S satisfying the condition above.
# Examples:
# 1. Given S = "ayxbx", the function should return 3. There are four possible splits of S: "a/yxbx", "ay/xbx", "ayx/bx" and "ayxb/x".
# Only "ay/xbx" does not fulfill the condition, so the answer is 3. Note that in "a/yxbx" the left part has 0 occurrences of 'x' and 'y', so it counts as correct split.
# 2. Given S = "xzzzy", the function should return 0.
# 3. Given S = "toyxmy", the function should return 5.
# 4. Given S = "apple", the function should return 4.
# Write an efficient algorithm for the following assumptions:
# N is an integer within the range [2..200,000];
# string S is made only of lowercase letters (a−z).
import re

def solution(S):
    N = len(S)
    if N not in range(2, 200001):
        return f"{N} should be in the range of 2-200,000"
    valid = r'^[a-z]+$'
    if not re.match(valid, S):
        return f"{S} Should only have lower case alphabetic characters"


    
    '''
    PREFIX_X and prefix_y are arrays of size N + 1. These arrays will store the cumulative (or prefix)
    count of 'x' and 'y' from the begining of the string up to each index
    * they are used to create a list with repeated elements 
    example lst = [0] * 5 the output will be [0,0,0,0,0]
    '''  
    prefix_x = [0] * (N + 1)
    prefix_y = [0] * (N + 1)
    # print(prefix_x)
    for i in range(1, N + 1):

        '''
        prefix_x[i] updates the count of 'x' charcters in the prefix up to the index i
        prefix_x[i - 1]this accesses the previous prefix count(i.e the number of x characters up to index i -1)
        (1 if S[i -1 ] == 'x' else 0) checks if the currrent character (S[i-1] is 'x' if it is we add 1 to the count otherwise we add 0)
        '''
        prefix_x[i] = prefix_x[i - 1] + (1 if S[i -1 ] == 'x' else 0)








# def solution(S):
#     N = len(S)
#     if N not in range(2, 200001):
#         return f"{N} should be in the range of 2-200,000"
    
#     # Precompute prefix counts for 'x' and 'y'
#     prefix_x = [0] * (N + 1)
#     prefix_y = [0] * (N + 1)
    
#     for i in range(1, N + 1):
#         prefix_x[i] = prefix_x[i - 1] + (1 if S[i - 1] == 'x' else 0)
#         prefix_y[i] = prefix_y[i - 1] + (1 if S[i - 1] == 'y' else 0)
    
#     result = 0
#     for i in range(1, N):
#         # Left part: S[0:i], Right part: S[i:N]
#         left_x = prefix_x[i] - prefix_x[0]
#         left_y = prefix_y[i] - prefix_y[0]
#         right_x = prefix_x[N] - prefix_x[i]
#         right_y = prefix_y[N] - prefix_y[i]
        
#         # Check if either left or right part satisfies the condition
#         if left_x == left_y or right_x == right_y:
#             result += 1
    
#     return result



print(solution("ayxbx"))
print(solution("xzzzy"))
print(solution("toyxmy"))
print(solution("apple"))