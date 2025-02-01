# Concatenation is an operation that joins strings. For example, the concatenation of strings "smart" and "phone" is "smartphone".
#  Concatenation can be expanded to more than two strings; for example, concatenating "co", "dil" and "ity" results in "codility".

# Given an array A consisting of strings, your function should calculate the length of the longest string S such that:
# S is a concatenation of some of the strings from A;
# every letter in S is different.
# Write a function:
# function solution(A);
# that, given an array A consisting of N strings, calculates the length of the longest string S fulfilling the conditions above.
#  If no such string exists, your function should return 0.
# Examples:
# 1. Given A = ["co", "dil", "ity"], your function should return 5. The resulting string S could be "codil", "dilco", "coity" or "ityco".
# 2. Given A = ["abc", "yyy", "def", "csv"], your function should return 6. The resulting string S could be "abcdef", "defabc", "defcsv" or "csvdef".
# 3. Given A = ["potato", "kayak", "banana", "racecar"], your function should return 0. It is impossible to choose any of these strings
#  as each of them contains repeating letters.
# 4. Given A = ["eva", "jqw", "tyn", "jan"], your function should return 9. One of the possible strings of this length is "evajqwtyn".
# Assume that:


# N is an integer within the range [1..8];
# each string in A consists of lowercase English letters;
# the sum of lengths of strings in A does not exceed 100.
# In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.
