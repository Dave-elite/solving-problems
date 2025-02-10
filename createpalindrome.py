# Write a function solution that, given a string S of length N, returns any palindrome which can be obtained by
# replacing all of the question marks in S by lowercase letters ('a'−'z'). If no palindrome can be obtained,
#  the function should return the string "NO".
# A palindrome is a string that reads the same both forwards and backwards. Some examples of palindromes are: "kayak", "radar", "mom".
# Examples:
# 1. Given S = "?ab??a", the function should return "aabbaa".
# 2. Given S = "bab??a", the function should return "NO".
# 3. Given S = "?a?", the function may return "aaa". It may also return "zaz", among other possible answers. The function is 
# supposed to return only one of the possible answers.
# Assume that:
# N is an integer within the range [1..1,000];
# string S consists only of lowercases letters ('a' − 'z') or '?'.
# In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.
import re
def solution(S):
    N = len(S)
    S = list(S)
    if N not in range(1, 1001):
        return f"{N} should be in the range of 1-1000"
    valid = r'^[a-z?]+$'
    if not re.match(valid, S):
        return f"{S} should only contain lowercase letters and question marks"
    for i in range(N // 2):
        print(i)
        right = S[i]
        left = S[N - i - 1]
        print(left)
    if right == '?' and left == '?':
        S[i] = 'a'
        S[N - i - 1] = 'a'
    elif right == '?':
        S[i] = S[N - i - 1]



    




















# import re
# def solution(S):
#     N = len(S)
#     s = list(S)
#     if N not in range(1, 1001):
#         return f"{N} should be in the range 1 - 1000"
#     valid = r'^[a-z?]+$'
#     if not re.match(valid, S):
#         return f"{S} should only contain lowercase letters and question marks"
#     for i in range(N // 2):
#         left = s[i]
#         right = s[N - i - 1]
        

#         if left == '?' and right == '?':
#             s[i] = 'a'
#             s[N - i - 1] = 'a'
#         elif left == '?':
#             s[i] = s[N - i - 1]
#         elif right == '?':
#             s[N - i - 1] = s[i]
#         elif right != left:
#             return "NO"

#     if N % 2 == 1 and s[N // 2] == '?':
#         s[N // 2] = 'b'
#     return ''.join(s)



































# import re
# def solution(str):
#     N = len(str)
#     S = list(str)
#     if N not in range(1, 1001):
#         return f"{N} should be in the range of 1 - 1000"
#     valid = r'^[a-z?]+$'
#     if not re.match(valid, str):
#         return f"{str} should only contain letters in lowercase and question marks"
#     for o in range(N // 2):
#         left = S[o]
#         right = S[N - o - 1]
#         # print(right)
#         if left == '?' and right == '?':
#             S[N - o - 1] = 'l'
#             S[o] = 'l'
#         elif left == '?':
#             S[o] = S[N - o - 1]
#         elif right == '?':
#             S[N - o - 1] = S[o]

#         elif right != left:
#             return "NO"
        
#     if N % 2 == 1 and S[N // 2] == '?':
#         S[N // 2] = 'b'
#     return ''.join(S)




















# import re
# def solution(Str):
#     N = len(Str)
#     if N not in range(1, 1001):
#         return f"{N} should be in the range of 1-1,000"
#     valid = r'^[a-z?]+$'
#     if not re.match(valid, Str):
#         return f"{Str} should only contain lowercase letters and question marks"

#     S = list(Str)
#     for i in range(N // 2):
#         left = S[i]
#         right = S[N - i - 1]
#         # print(left)
#         if left == '?' and right == '?':
#             S[i] = 'a' 
#             S[N - i - 1] = 'a' 

#         elif right == '?':
#             S[N - i - 1] = S[i]
#         elif left == '?':
#             S[i] = S[N - i - 1]

#         elif left != right:
#             return "NO"
    
#     if N % 2 == 1 and S[N // 2] == '?':
#         S[N // 2] == 'b'
#     return''.join(S)




























# import re
# def solution(Str):
#     N = len(Str)
#     S = list(Str)

#     if N not in range(1, 1000):
#         return f"{N} should be in the range of 1-1000"
#     valid = r'^[a-z?]+$'
#     if not re.match(valid, Str):
#         return f"{N} should only contain lowercase letters and question marks"
    
#     for i in range(N // 2):
#         # print(i)
#         left = S[i]
#         right = S[N - i - 1]

#         if left == '?' and right == '?':
#             S[i] = 'a'
#             S[N - i - 1] = 'a'

#         elif left == '?':
#             S[i] = S[N - i - 1]

#         elif right == '?':
#             S[N - i - 1] = S[i]

#         elif right != left:
#             return 'NO'
        
#     #sort the character in the middel for the string with odd length 
#     if N % 2 == 1 and S[N // 2] == '?':
#         S[N // 2] = 'b'

#     return ''.join(S)







print(solution("?ab??a"))
print(solution("bab??a"))
print(solution("?a?"))



















































# import re
# def palindrome(Str):
#     N = len(Str)
#     S = list(Str)

#     if N not in range(1, 1000):
#         return f"{N} should be in the range of 1-1000"

#     valid = "^[a-z?]+$"
#     if not re.match(valid, Str):
#         return "the str should only contain lowercase letters and a question mark"

#     for i in range(N // 2):
#         # print(i)

#         left = S[i]
#         right = S[N - i -1]
#         print(right)

#         if left == '?' and right == '?':
#             S[i] = 'a'
#             S[N - i -1] = 'a'
#         elif left == '?':
#             S[i] = S[N - i -1]
#         elif right == '?':
#             S[N - i -1] = S[i]
#         elif right != left:
#             return "NO"
#             #DONE
#     #for the str with odd len 
#     # and the str has a question mark in the middle of the str we change it to a lowercase letter

#     if N % 2 == 1 and S[N // 2] == "?":
#         S[N // 2] = 'a'

#     return ''.join(S)  




# print(palindrome("?ab??a"))
# print(palindrome("bab??a"))
# print(palindrome("?a?"))


# def solution(str):
#     N = len(str)
#     S = list(str)
#     # print(S)

#     for i in range(N // 2):
#         # print(i)
#         left = S[i]
#         # print(left)
#         right = S[N - i - 1]
#         # print(right)

#         # check if both of the sides have the question marks
#         if left == '?' and right == '?':
#             S[i] = 'a'
#             S[N - i - 1] = 'a'
#         elif left == '?':
#             S[i] = S[N - i - 1]
#         elif right == '?':
#             S[N - i - 1] = S[i]

#         elif right != left:
#             return "NO"
        
#     # THE ODD NUMBER IS SUPPOSSED TO HAVE A MIDDLE VALUE
#     #if the middle value is a question mark we replace it with any letter

#     if  N % 2 == 1 and S[N // 2] == '?':
#         S[N // 2] = 'b'

#     return ''.join(S)




# print(solution("?ab??a"))
# print(solution("bab??a"))
# print(solution("?a?"))




# import re
# def palindrome(str):
#     N = len(str)

#     S = list(str)

#     for i in range(N // 2):
#         left = S[i]
#         right = S[N - i - 1]
#         # print(right)
        
#         # print(left)
#         # if both characters are question marks replace them with the same letter

#         if left == '?' and right == '?':
#             S[i] = 'a'
#             S[N - i - 1] = 'a'

#         elif left == '?':
#             S[i] = right
#         elif right == '?':
#             S[N - i - 1] = left

#         elif left != right:
#             return "NO"
        
#     #If the string length is odd, we do not need to check the middle charcter 
#     #But if it's a '?', we can replace it with any letter, eg a

#     if N % 2 == 1 and S[N // 2] == '?':
#         S[N // 2] = 'a'

#     return ''.join(S)



# print(palindrome("?ab??a"))
# print(palindrome("bab??a"))
# print(palindrome("?a?"))

