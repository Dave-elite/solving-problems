# You have just rolled a dice several times. The N roll results that you remember are described by an array A.
#  However, there are F rolls whose results you have forgotten. The arithmetic mean of all of the roll 
# results (the sum of all the roll results divided by the number of rolls) equals M.
# What are the possible results of the missing rolls?
# Write a function:
# def solution(A, F, M)
# that, given an array A of length N, an integer F and an integer M, returns an array containing possible results of the missed rolls. The returned array should contain F integers from 1 to 6 (valid dice rolls). If such an array does not exist then the function should return [0].
# Examples:
# 1. Given A = [3, 2, 4, 3], F = 2, M = 4, your function should return [6, 6]. The arithmetic mean of all the rolls is (3 + 2 + 4 + 3 + 6 + 6) / 6 = 24 / 6 = 4.
# 2. Given A = [1, 5, 6], F = 4, M = 3, your function may return [2, 1, 2, 4] or [6, 1, 1, 1] (among others).
# 3. Given A = [1, 2, 3, 4], F = 4, M = 6, your function should return [0]. It is not possible to obtain such a mean.
# 4. Given A = [6, 1], F = 1, M = 1, your function should return [0]. It is not possible to obtain such a mean.
# Write an efficient algorithm for the following assumptions:
# N and F are integers within the range [1..100,000];
# each element of array A is an integer within the range [1..6];
# M is an integer within the range [1..6].
def solution(A, F, M):
    N = len(A)
    total_sum = M * (N + F)
    known_sum = sum(A)
    # print(known_sum)
    forgotten_sum = total_sum - known_sum
    
    if forgotten_sum < F or forgotten_sum > F * 6:
        return [0]
    #start by setting all f rolls to 1
    result = F * [1]
    #Since we have made each roll to be 1 above this means that F will be the sum of the rolls in result since all of them are one
    current_sum = F
    # print(result)
    #the addition sum needed to reach the forgotten sum after initializing all rolls to 1
    remaining_sum = forgotten_sum - current_sum
    #the goal of this loop is to distribute the remaining_sum.Each roll must be between 1 and 6, so we need
    # to ensure that we don't exceed these bounds while disturbing the sum
    '''
    We started by initializing all F missing rolls to 1. This is the minimum value a dice roll can take
    Since all rolls are intialized to 1, the sum of these rolls is F.

    '''
    for i in range(F):
        # print(i)
        #We can add atlears 5 to a roll because each roll is already 1, and the maximum value a roll can take 6.
        #So, the maximum value a roll can take is 5. 
        add = min(5, remaining_sum)
        # if remaining_addition is less than 5 we add to the result list
        result[i] += add
        #after adding less the number antered from the remaining_sum
        remaining_sum -= add
        # print(result)
        if remaining_sum == 0:
            break
    #This checks whether the remaining_sum has been fully distributed across f missing dice_rolls
    # if there is still some remaining_addition left after it across rolls it mrans it's impossible to acieve the required sum    
    if remaining_sum > 0:
        return [0]

    return result

































# def solution(A, F, M):
#     N = len(A)
    
#     # Calculate the total required sum of all rolls
#     total_required_sum = M * (N + F)
#     sum_of_known_rolls = sum(A)
    
#     # Calculate the sum we need from the missing rolls
#     missing_sum = total_required_sum - sum_of_known_rolls
    
#     # Check if it's possible to get the missing_sum with F rolls between 1 and 6
#     if missing_sum < F or missing_sum > 6 * F:
#         return [0]
    
#     # Start with F rolls all set to 1
#     result = [1] * F
#     current_sum = F  # Since all are initialized to 1, the sum is F initially
    
#     # Now we need to reach the missing_sum, so we need to add (missing_sum - current_sum)
#     remaining_addition = missing_sum - current_sum
    
#     # Distribute the remaining addition across the rolls
#     for i in range(F):
#         # Add as much as possible to each roll (max is 5 because each roll is 1 initially)
#         add = min(5, remaining_addition)
#         result[i] += add
#         remaining_addition -= add
        
#         # If we've distributed all the remaining addition, we can stop
#         if remaining_addition == 0:
#             break
    
#     # If we still have remaining addition to distribute, it's impossible
#     if remaining_addition > 0:
#         return [0]
    
#     return result





























# def solution(A, F, M):
#     N = len(A)
#     if N not in range(1, 100001):
#         return f"{N}should be in the range 1 - 100,000"
#     if F not in range(1, 100001):
#         return f"{F} should be in the range of 1 - 100,000"
#     if M not in range(1, 7):
#         return f"{M} should be in the range of 1 - 7"
#     for i in A:
#         if i not in range(1, 7):
#             return f"{i} should be in the range of 1 - 6"
        
#     total_rolls = M * (N + F)
#     known_total = sum(A)
#     # print(known_total)
#     forgortten_sum = total_rolls - known_total

#     if forgortten_sum < F and forgortten_sum < F * 6:
#         return [0]

    

#     current_rolls = N * [1]
#     current_sum = F
#     # print(current_rolls)
#     remaining_sum = forgortten_sum - current_sum
#     # print(remaining_sum)
    
#     for i in range(F):
#         add = min(5, remaining_sum)
#         current_rolls[i] += add
#         remaining_sum -= add
#         # print(remaining_sum)
#         if remaining_sum == 0:
#             break
#     return current_rolls if remaining_sum == 0 else [0]












# def solution(A, F, M):
#     N =len(A)
#     if N not in range(1, 100001):
#         f"{N} should be in the range of 1 - 100,000"
#     if F not in range(1, 100001):
#         f"{F} should be in the range of 1 - 100,000"
    
#     if M not in range(1, 7):
#         f"{M} should be in the range of 1 - 6"
#     for i in A:
#         if i not in range(1,7):
#             f"{i} should be in the range of 1- 6"

#     known_sum = sum(A)
#     total_rolls = M * (N + F)
#     # print(known_sum)
#     forgotten_sum = total_rolls - known_sum

#     '''
#     this checks if the sum of the forgotten rolls is possible
#     each forgotten roll must be between 1 and 6
#     the minimum possible sum of the F forgotten rolls is F (if all rolls are 1)
#     the maximum possible sum of F forgotten rolls is F * 6 (if all rolls are 6)
#     if the forgotten sum is less than F and greater than F * 6 It is impossible to achieve the desired mean
#     so return, [0]
#     '''
#     if forgotten_sum < F and forgotten_sum < F * 6:
#         return[0]

#     current_roll = [1] * F
#     current_sum = F
#     # print(current_roll)
#     remaining_sum = forgotten_sum - current_sum
#     # print(current_roll)

#     for i in range(F):
#         add = min(5, remaining_sum)
#         # print(add)
#         current_roll[i] += add
#         remaining_sum -= add
#         # print(remaining_sum)
#         if remaining_sum == 0:
#             break
#     return current_roll if remaining_sum == 0 else [0]

    

    

        
    




























# def solution(A, F, M):
#     N = len(A)
#     if N not in range(1, 100001):
#         return f"{N} should be in the range of 1 - 100,000"

#     if F not in range(1, 100001):
#         return f"{F} should be in the range of 1 - 100,000"

#     if M not in range(1, 7):
#         return f"{M} should be in the range of 1 - 6"
#     for i in A:
#         if i not in range(1, 7):
#             return f"{i} should be in the rangeof 1-6"
#     known_sum = sum(A)
#     total_sum = M * (N + F)
#     forgotten_sum = total_sum - known_sum

#     if forgotten_sum < F or forgotten_sum > F * 6:
#         return [0]

#     rolls = [1] * F
#     current_sum = F
#     remaining_sum = forgotten_sum - current_sum

#     for i in range(F):
#         add = min(5, remaining_sum)
#         rolls[i] += add
#         remaining_sum -= add
#         if remaining_sum == 0:
#             break
#     return rolls if remaining_sum == 0 else [0]





















# def solution(A, F, M):
#     N = len(A)
#     if N not in range(1, 100001):
#         return f"{N} should be in the range of 1 - 100,000"
#     if F not in range(1, 100001):
#         return f"{F} should be in the range of 1 - 100,000"
#     if M not in range(1, 7):
#         return f"{M} should be in the range of 1 - 6"
#     for i in A:
#         if i not in range(1, 7):
#             return f"{i} should be in the range of 1 - 6"

#     '''
#     known sum is the total value of the values in the array A which represents the sum of the rolls you remember
#     total sum is the sum of all rolls known and forgotten that would be give you the desired mean M
#     It is calculated by multiplying the desired mean M by the total number of rolls N (Length of the array) + F(length of the forgotten) and M being the mean = M * (N + F)
#     With the total sum and the sum of the forgotten sum you are able to remember the total number of the forgotten_sum
#     which is forgotten_sum = total_sum - known_sum
#     '''
#     known_sum = sum(A)
#     print(known_sum)
#     total_sum = M * (N + F)
#     forgotten_sum = total_sum - known_sum

#     '''
#     each roll must be a number between 1 and 6, inclusive. therefore the sum of the 
#     forgotten rolls must fall within specific range which is the btw f * 1 and f * 6
#     '''
#     if forgotten_sum < F * 1 or forgotten_sum > 6 * F:
#         return [0]

#     '''
#     rolls = [1] * F initializes a list called rolls that will hold the values of the forgotten rolls. 
#     [1] * F creates a list of F elements each initialized to 1
#     each roll can be between 1 and 6 and we start by assuming the smallest possible value(1) for each forgotten role
#     example if F = 3 THEN rolls would initially be [1,1,1]
#     The current sum is the total sum of the forgotten rolls which you've just initialized
#     since the list rolls contains F elements and each element is initialized to 1, the sum of these elements is simply F
#     Remaining sum is the difference between forgotten_sum and current_sum, which is the additinal value we need to distribute
#     across the F forgotten rolls
#     '''
#     rolls = [1] * F
#     current_sum = F
#     remaining_sum = forgotten_sum - current_sum

#     '''
#     Distribute the remaining_sum across the F forgotten rolls
#     for each roll it adds as much as possible but not more than 5(since the roll cannot
#     exceed 6, and it was already inititialized as 1)
#     it reduces the remaninng_sum by the amount added, and if the remaining sum becomes zero, it breaks ouf of the 
#     loop, as no further distribution is needed.
#     '''
#     for i in range(F):
#         '''
#         the min() function is to ensure you do this by choosing the smaller of 5 and remaining_sum
#         '''
#         add = min(5, remaining_sum)
#         rolls[i] += add
#         remaining_sum -= add

#         if remaining_sum == 0:
#             break
#     return rolls if remaining_sum == 0 else [0]
        


# Example 1
A = [3, 2, 4, 3]
F = 2
M = 4
print(solution(A, F, M))  # Expected output: [6, 6]

# Example 2
A = [1, 5, 6]
F = 4
M = 3
print(solution(A, F, M))  # Expected output: Possible outputs like [2, 1, 2, 4] or [6, 1, 1, 1] etc.

# Example 3
A = [1, 2, 3, 4]
F = 4
M = 6
print(solution(A, F, M))  # Expected output: [0]

# Example 4
A = [6, 1]
F = 1
M = 1
print(solution(A, F, M))  # Expected output: [0]