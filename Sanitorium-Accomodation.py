# There are N guests (numbered from 0 to N-1) in a sanatorium waiting to be assigned a room. In each room, any number of guests can be accommodated. However, not all guests like to have a lot of roommates.
# You are given an array A of N integers: the K-th guest wants to be in a room that contains at most A[K] guests, including themselves.
# Write a function:
# def solution(A)
# that, given the array A, returns the minimum number of rooms needed to accommodate all guests.
# Examples:
# 1. Given A = [1, 1, 1, 1, 1], your function should return 5. Each guest should be accommodated in their own separate room.
# 2. Given A = [2, 1, 4], your function should return 2. The second guest should be accommodated in one room and the other two guests in another room.
# 3. Given A = [2, 7, 2, 9, 8], your function should return 2. The first and the third guests should be accommodated in one room and the other three guests in another room.
# 4. Given A = [7, 3, 1, 1, 4, 5, 4, 9], your function should return 4. The guests can be accommodated as follows: the first two guests in one room, the third and the fourth guests in two single rooms, and the other guests in another room.
# Write an efficient algorithm for the following assumptions:
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [1..100,000].

def solution(A):
    N = len(A)
    
    if N not in range(1, 100001):
        return f'{N} should be in the range of 1 - 100,000'
    for i in A:
        if i not in range(1, 100001):
            return f"{i} should be in the range of 1 - 100,000"
        
    sorted_guests = sorted(enumerate(A), key=lambda x: x[1])
    rooms = []
    # print(sorted_guests)

    for guest_indx, max_guests in sorted_guests:
        placed = False

        for room in rooms:
            if len(room) < min(A[k] for k in room):
                rooms.append(guest_indx)
                placed = True
            if not placed:
                rooms.append([guest_indx])
    return len(rooms)




















# def solution(A):
#     N = len(A)
#     if N not in range(1, 100001):
#         return f"{N} should be in the range 1- 100,000"
#     for i in A:
#         if i not in range(1, 100001):
#             return f"{i} should be in the range 1 - 100,000"
        
#     ''''
#     enumarate(A) pairs each guests with their index and room capacity. for example, if A
#     = [3, 1, 2] then enumarate(A) gives [(0, 3), (1, 1)]
#     sorted(..., key=lambda x : x[1]) sorts the list based on the second element of each tuple which is the value insted of using the index
#     '''
        
#     sorted_guests = sorted(enumerate(A), key=lambda x : x[1])

#     rooms = []

#     print(sorted_guests)
#     for guest_idx, max_guests in sorted_guests:
#         placed = False

#         for room in rooms:
#          if len(room) < min(A[k] for k in room):
#             room.append(guest_idx)
#             placed = True
#         if not placed:
#            rooms.append([guest_idx])

#     return len(rooms)


































# def solution(A):
#     N = len(A)
#     if N not in range(1, 100001):
#         return f"{N} should be in the range of 1 - 100,000"
#     for i in A:
#         if i not in range(1, 100001):
#             return f"{i} should be in the range of 1 - 100,000"
#     '''
#     the array A is sorted in ascending order based on the values in A. However, since we need to retain the original indices of guests
#     (since they are important for later placing them in rooms), the enumarate(A) function is used. it produces pairs of (index, value) for each guest,
#     and then it sorts these pairs by the value(maximum number of guests each guests is willing to accomodate) This ensures that guests who are more restictive (want fewer roomates
#     ) are processed first
#     the key argument in the sorted function specifues a function that determines the value to use for sorting
#     Here, lambda x: x[1] is an anonymous function (a lambda function) that takes a tuple x as input and returns x[1] 
#     the second element of the tuple (which is the value from the array A)
#     IN simpler terms, this is telling python to sort the list of tuples based on the second element of each tuple (the value from the original array A)
#     '''
        
#     sorted_guests = sorted(enumerate(A), key=lambda x: x[1])

#     rooms = []
   

#     for guest_idx, max_guests in sorted_guests:
#         placed = False

#         for room in rooms:
#             if len(room) < min(A[k] for k in room):
#                 room.append(guest_idx)
#                 placed = True
#                 break
#         if not placed:
#             rooms.append([guest_idx])

#     return len(rooms)

        































# def solution(A):
#     N = len(A)
#     if N not in range(1, 100001):
#         return f"{N} should be in the range of 1-100,000"

#     for i in A:
#         if i not in range(1, 100001):
#             return f"{i} should be in the range of 1-100,000"

#         #sort the array
#         sorted_guests = sorted(enumerate(A), key=lambda x: x[1])
        

#         #define an empty array for rooms
#         rooms = []


#         #create a for loop for the sorted guests for its tuples where there is the index and the max guest limit which is charactarized by the value of tuple
#         for guest_index, max_guest in sorted_guests:
#             posted = False

#             for room in rooms:
#                 if len(room) < min(A[k] for k in room):
#                     room.append(guest_index)
#                     posted = True
#                     break

#             if not posted:
#                     rooms.append([guest_index])
#         return len(rooms)









# def solution(A):
#     N =len(A)
#     if N not in range(1, 100001):
#         return f"{N} should be in the range of 1 - 100,000"

#     for i in A:
#         if i not in range(1, 100001):
#             return f"{i} should be in the range of 1 - 100,000"

#         '''
#         lamba is an anonymous function that is used when wants a function to be used in a short period of time 
#         lambda x represents each element in the list element and x[1] means we are looking at the second element since the value after enumaration is the second element
#         '''

#         sorted_guests = sorted(enumerate(A), key=lambda x: x[1])

#         #initializes an empty list rooms which is intended to keep track of the rooms and their guests placements
#         rooms = []

#         #the loop iterates over sorted_guests where each element is a tuple of the index and the value which also repesents the value of the max requirments of the guest in terms of roomates 
#         for guest_idx, maxguests in sorted_guests:
#             placed  = False

#             for room in rooms:
#                 if len(room) < min(A[k] for k in room):
#                     room.append(guest_idx)
#                     placed = True
#                     break
#             if not placed:
#                     rooms.append([guest_idx])

#         return len(rooms)




















# def solution(A):
#     N = len(A)
#     if N < 1 or N > 100_000:
#         return f"{N} should be in the range of 1-100,000"
    
#     for i in A: 
#         if i not in range(1, 100001):
#             return f"{i} should be in the range of 1-100,000"
#         ''''sort the guests by their tolerance level (ascending)
#         This makes it easier to process least torelant guests first
#         enumarate() is a built-in Python function that adds a counter (index to an iterable (like a list) and returns an iterator in tuples)
#         in our case A is a list (lets assume it contains the preference of the guests where each number in the list represents a guest tolerance for the maximun number of guests)
#         they can share a room with.
#         For example A = [2,1,4] when you enumarate you get 
#         output: [(0,2), (1, 1), (2,4)]
#         thus enumarate gives us pairs on (index, value) 
#         Sorted(): built in python function that sorts any iterable (like a list ) into a new list.
#         It returns a new list with the elements ordered in a specified way
#         key=lambda x: x[1]
#         the key element allows you to specify a function that will be applied to each element in the list before sorting
#         lambda x: x[1] this is a lambda function which is anonymous (unnamed) function.
#         A lambda function in python is used when you need a simple function for a short period 
#         in this case lambda x: x[1] means 
#                 x represents each element in the list 
#                 x[1] means we are looking at the second item in each tupke (since enumarate produces tuples of the form (index, value)). 
#         '''
        
#         # print(enumerate(A))
#         sorted_guests = sorted(enumerate(A), key=lambda x: x[1])
#         #list will store rooms, where each room is a list of guests indices
#         rooms = []
#         '''
#             we create an empty list rooms. This will hold the rooms, where each room is represented as list of guest indices
#             for example, after the guest assignment, rooms might look like this
#             rooms = [[1,2], [0]] this means guest 1 and guest 2 are in one room and guest o are in a separate room
#             we loop through the sorted list sorted_guests and attempt to place each guest in a room guest_idx is the index of the current guests,
#             and max_guests is the tolerance of that guest 
#             the places variable is initially set to false indicating that the guest hasn't placed a room yet

            
#             '''
#         for guest_idx, max_guests in sorted_guests:
#             #try to place guest in an existing room
#             placed = False

#             #check each existing room

#             '''
#             inside the loop, we iterate through each room in rooms. we are checking if we can add the current guest to an existing room
#             the condition len(room) < min(A[i] for i in room) checks if the room can accomodate more guests without violating the tolerance of any guests already in the room
#             len(room) gives the current number of guests in the room 
#             min(A[i] for i in room ) finds the smallest tolerance among the guests in the room 
#             this is the maximum number of people that any guests in the room is willing to tolerate
#             if the room can accomodate more guests(the current room size is less than the minimum tolerance ) the current gusts(guest_idx)is added to that toom and placeed set ast true
#             If the guest could not be places in any existing room (placed is still false), a new room is created 
#             and the current guests is places in that room as the first occupant
#             '''
            
#             for room in rooms:
#                 if len(room) < min(A[i] for i in room):
#                     room.append(guest_idx)
#                     placed = True
#                     break
#             if not placed:
#                 rooms.append([guest_idx])
#         return len(rooms)
    
  

# def solution(A):
#     N = len(A)
#     roomcount = 0
#     seen = set()
#     duplicates = set()
#     if N not in range(1, 100000):
#         return f"{N} should be in the range of 1-100,000"
#     for i in A:
#         # print(i)
#         if i not in range(1, 100000):
#             return f"{i} should be in the range of 1-100,000"
#         if i == 1:
#             roomcount += 1
#         elif i in seen:
#             duplicates.add(i)
#         else:
#             seen.add(i)

#         if i in duplicates:
#             roomcount += 1
#     # print(duplicates)
#     return roomcount

    
    



print(solution([1, 1, 1, 1, 1]))
print(solution([2, 1, 4]))
print(solution([2, 7, 2, 9, 8]))
print(solution([7, 3, 1, 1, 4, 5, 4, 9]))

