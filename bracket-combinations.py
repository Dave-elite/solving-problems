# Bracket Combinations
# Have the function BracketCombinations(num) read num which will be an integer greater than or equal to zero, and return 
# the number of valid combinations that can be formed with num pairs of parentheses. For example, if the input is 3,
#  then the possible combinations of 3 pairs of parenthesis, namely: ()()(), are ()()(), ()(()), (())(), ((())), and (()()). 
#  There are 5 total combinations when the input is 3, so your program should return 5.
# Examples
# Input: 3
# Output: 5
# Input: 2
# Output: 2

def BracketCobmninations(num):
  if num == 0:
    return 1
  count = 0

  for i in range(num):
    BracketCobmninations(i)
    count += BracketCobmninations(i) * BracketCobmninations(num - i - 1)
print(BracketCobmninations(input()))


















# def BracketCombinations(num):
  
#   #if the num argument is 0 then this means there are no pairs of parenthesis to arrange.
#   #The only solid comninations is an empty string which count as 1 valid arrangemnent so we return 1
#   if num == 0:
#     return 1
  

  # count = 0
  # for i in range(num):
  #   # print(BracketCombinations(i))
  #   # print(BracketCombinations(num - 1 - i))
  #   count += BracketCombinations(i) * BracketCombinations(num - 1 - i)
  # return count




# keep this function call here 
# print(BracketCombinations(input()))