# There is a road consisting of N segments, numbered from 0 to N-1, represented by a string S. Segment S[K] of the road may contain a pothole, 
# denoted by a single uppercase "X" character, or may be a good segment without any potholes, denoted by a single dot, ".".
# For example, string ".X..X" means that there are two potholes in total in the road: one is located in segment S[1] and one in segment S[4].
#  All other segments are good.
# The road fixing machine can patch over three consecutive segments at once with asphalt and repair all the potholes located within each of these segments.
#  Good or already repaired segments remain good after patching them.
# Your task is to compute the minimum number of patches required to repair all the potholes in the road.
# Write a function:
# function solution(S);
# that, given a string S of length N, returns the minimum number of patches required to repair all the potholes.
# Examples:
# 1. Given S = ".X..X", your function should return 2. The road fixing machine could patch, for example, segments 0-2 and 2-4.
# 2. Given S = "X.XXXXX.X.", your function should return 3. The road fixing machine could patch, for example, segments 0-2, 3-5 and 6-8.
# 3. Given S = "XX.XXX..", your function should return 2. The road fixing machine could patch, for example, segments 0-2 and 3-5.
# 4. Given S = "XXXX", your function should return 2. The road fixing machine could patch, for example, segments 0-2 and 1-3.
# Write an efficient algorithm for the following assumptions:
# N is an integer within the range [3..100,000];
# string S is made only of the characters '.' and/or 'X'.
def solution(S):
    N = len(S)
    # print(N)
    patches = 0
    for r in range(0, N, 3):
        # print(r)
        pairs = S[r: r+3]
        # print(pairs)
        if 'X' in pairs:
            patches += 1
    return patches




























# import re
# def solution(S):
#     N = len(S)
#     # S = list(S)
#     group = []
#     count = 0
#     if N not in range(3, 100001):
#         return f"{N} should be in the range of 3 - 100,000"
#     valid = r'^[.X]+$'
#     if not re.match(valid, S):
#         return f"{S} should only contain characters '. and X characters"
#     for u in range(0, N, 3):
#         # print(u)
#         k = S[u: u+3]
#         # print(k)
#         group.append(k)
#     # print(group)
#     for i in group:
#         # print(i)
#         if 'X' in i:
#             count += 1
#     return count





















# import re
# def solution(S):
#     N = len(S)
#     # S = list(S)
#     batches = []
#     patches = 0
#     if N not in range(3, 100001):
#         return f"{N} Should be in the range 3 - 100,000"
#     valid = r'^[.X]+$'
#     if not re.match(valid, S):
#         return f"{S} should only contain X and . characters"
#     for i in range(0, N, 3):
#         batches.append(S[i : i + 3])
#     for k in batches:
#         # print(k)
#         if 'X' in k:
#             patches += 1
#     return patches









































# import re
# def solution(s):
#     patches_repaired = 0
#     S = list(s)
#     N = len(s)
#     batches = []
#     if N not in range(3, 100001):
#         return f"{N} should be in the range of 3 - 100,000"
#     valid = r'^[.X]+$'
#     if not re.match(valid, s):
#         return f"{s} should only contain x and . characters"
#     for i in range(0, N, 3):
#         batches.append(S[i: i + 3])
#     for k in batches:
#         # print(k)
#         if 'X' in k:
#             patches_repaired += 1
#     return patches_repaired

    
print(solution(".X..X"))
print(solution("X.XXXXX.X."))
print(solution("XX.XXX.."))
print(solution("XXXX"))
