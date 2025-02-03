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
import re
import itertools
def solution(A):
    N = len(A)
    possible_str = []
    
    
    # print(N)
    if N not in range(1,9):
        return f"{N} should be in the range of 1-8"
    total_length = sum(len(item) for item in A)
    if total_length > 100:
        return f"the sum of the length of the strigns in A exceeds 100. total length is {total_length}"
    # print(total_length)
    valid = r'^[a-z]+$'
    for item in A:
        if not re.fullmatch(valid, item):
            return f"{A} should only contain lowercase english letters"

    '''
    python has a built-in module called itertools that provide a set of fast, memeory efficient tools for working with iterators
    one of the functions we use is itertools.produect
    itertools.products is a function in pythons itertools module that computes the cartesian
    product og input iterables. in simpler terms it generates all possible combinations(or pairs, tripples)
    of elementss from the given iterables. its like taking every combination of elements from a set, with the option to repeat the elements if needed
    This is extremmely useful in many scenarios, particulary when you need to explore or iterate over all possible  combinations of values

    '''
    # pairs = itertools.product(A, repeat=2)
    # #concatenate all possible pairs
    # concatenate_pairs = [''.join(pair) for pair in pairs]
    # # print(concatenate_pairs)
    # concatenate_pairs = list([set(concatenate_pairs)])
    # seen = set()
    # unique_pairs = []
    # for item in concatenate_pairs:
    #     if item not in seen:
    #         unique_pairs.append(item)
    #         seen.add(item)
    # for possible_s in unique_pairs:
    #     # print(possible_s)
    #     possible_str.append(possible_s)
    #     print(possible_str)

    '''
    itertool comninations from the function itertools module generates all possible combinations of r elements
    from the iterable without repetiton unlike itertool product which allows repetions
    it produces each comnbination as a tuple
    
    '''
    max_length = 0
    ''''
    loop iterates over all possible lengths(r) of combinations of strings
    
    '''
    for r in range(1, N + 1):
        for combo in itertools.combinations(A, r):
            concatenated = ''.join(combo)
            # print(concatenated)
            if len(set(concatenated)) == len(concatenated):
                max_length = max(max_length, len(concatenated))

    return max_length

            
 
        
        
        
        





print(solution(["co", "dil", "ity"]))
print(solution(["abc", "yyy", "def", "csv"]))
print(solution(["potato", "kayak", "banana", "racecar"]))
print(solution(["eva", "jqw", "tyn", "jan"]))

