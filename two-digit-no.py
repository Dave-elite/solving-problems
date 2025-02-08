# Posted Oct 17, 2024
# Assigned
# You are given a string S consisting of N digits. What is the largest sum of two two-digit fragments of S?
#  The selected fragments cannot overlap.
# Write a function:
# def solution(S)
# that, given a string S, returns the largest sum of two two-digit numbers that are non-overlapping fragments of S.
# Examples:
# 1. Given S = "43798", the function should return 141. The chosen fragments are "43" and "98": "43 7 98"
# 2. Given S = "00101", the function should return 10. The chosen fragments are "00" and "10": "00 10 1". 
# Note that fragments "01" and "10" cannot be chosen as they overlap.

# 3. Given S = "0332331", the function should return 66. The chosen fragments are "33" and "33": "0 33 2 33 1".
# 4. Given S = "00331", the function should return 34. The chosen fragments are "03" and "31": "0 03 31"
# Assume that:
# N is an integer within the range [4..100];
# string S is made only of digits (0−9).
# In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.
import re

def solution(S):
    N = len(S)
    last_digit = None
    result = []
    
    # Check if the length of the string is within the valid range
    if N not in range(4, 101):
        return f"{N} should be in the range of 4 - 100"
    
    # Check if the string contains only digits
    valid = r'^[0-9]+$'
    if not re.match(valid, S):
        return f"{S} should only contain 0-9 digits"
    
    # Loop through the string to form pairs
    for i in range(N - 1):
        current_pair = S[i: i + 2]
        
        # If the first digit is not the same as the last digit, print the first digit
        if current_pair[0] != last_digit:
            result.append(current_pair[0])
        
        # If the current pair has the same digit (overlap), just print the second digit
        if current_pair[0] == current_pair[1]:
            last_digit = current_pair[1]
            break  # Stop here since we can't use overlapping digits
        else:
            last_digit = current_pair[1]
        
        # If it's the last valid digit, print it
        if i + 1 == N - 2:
            result.append(current_pair[1])

    return ', '.join(result)  # Return a comma-separated string of results

# Test the function
print(solution("43798"))  # Expected: "43, 7, 98"
print(solution("00101"))  # Expected: "0, 1"
print(solution("0332331"))  # Expected: "0, 3, 2, 3, 1"
print(solution("00331"))  # Expected: "0, 3, 1"
def solution(S):
    N = len(S)
    
    # List to hold all possible two-digit fragments
    two_digit_numbers = []
    
    # Extract all two-digit numbers from the string
    for i in range(N - 1):
        two_digit_numbers.append(int(S[i:i+2]))
    
    max_sum = 0  # Variable to store the maximum sum of two non-overlapping pairs
    
    # Loop through all possible pairs of two-digit numbers
    for i in range(len(two_digit_numbers) - 1):
        for j in range(i + 1, len(two_digit_numbers)):
            # Check if the two pairs are non-overlapping
            if i + 1 < j:  # Ensure there's no overlap (i.e., i + 1 must be before j)
                # Calculate the sum of these two pairs
                pair_sum = two_digit_numbers[i] + two_digit_numbers[j]
                # Update max_sum if the current pair's sum is larger
                max_sum = max(max_sum, pair_sum)
    
    return max_sum


# Test the function with the given examples
print(solution("43798"))  # Expected: 141 (43 + 98)
print(solution("00101"))  # Expected: 10 (00 + 10)
print(solution("0332331"))  # Expected: 66 (33 + 33)
print(solution("00331"))  # Expected: 34 (03 + 31)

