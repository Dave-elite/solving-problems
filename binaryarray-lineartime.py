# Sort binary array in linear time
# Given a binary array, sort it in linear time and constant space. 
# The output should print all zeros, followed by all ones.

# For example,

# Input:  { 1, 0, 1, 0, 1, 0, 0, 1 } Output: { 0, 0, 0, 0, 1, 1, 1, 1 }


# def solution(A):
#     N = len(A)

#     arrange = sorted(A)
#     return arrange

def solution(A):
    
    '''
    counting how many zeros are there in the list also the zeros is a variable for the count of the zeros

    '''
    zeros = A.count(0)
    #the variable k is initialized to 0. This variable will be used to keep track of the insed in the list 
    
    k = 0
    # print(zeros)
    while zeros:
        A[k] = 0
        zeros = zeros - 1
        k = k + 1
    for k in range(k, len(A)):
        A[k] = 1
    print(A)
 

























# def solution(A):
#     zeros = A.count(0)
#     print(zeros)
#     k = 0
#     while zeros:
#         A[k] = 0
#         zeros = zeros - 1
#         k = k + 1
#     for k in range(k, len(A)):
#         A[k] = 1
#     print(A)


























# def solution(A):
#     # count number of 0's
#     zeros = A.count(0)
#     print(zeros)
#     #put the zeros at the beginging
#     '''
#     variable k is initialized to 0. This will be used as the index to place the zeros at the 
#     begining of the list 
#     '''
#     k = 0
#     '''
#     the while loop runs as longs there are zeros < 0 in each iterations of the loop 
#     A[k] = 0 it sets k-th element of A to 0.
#     zeros = zeros - 1 : this decreases the count of the remaining zeros
#     k = k + 1 it increments k moving to the next position in the list for placing the next 0.

#     '''
#     while zeros:
#         A[k] = 0
        
#         zeros = zeros - 1
#         k = k + 1
#         # print(k)
#     '''
#     After the while loop the remaining elements in the list (starting from the index k) are set to 1 this done using for loop

#     '''
#     for k in range(k, len(A)):
#         A[k] = 1
    
#     sorted(A)
#     print(A)

print(solution([ 1, 0, 1, 0, 1, 0, 0, 1 ]))