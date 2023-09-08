##########################################
#   Author: Niclas Alexander Pedersen    #
#      Challenge: Two Sum Leetcode       #
#           Written: 08/09/23            #
#            Language: Python            #
#                                        #
##########################################


nums = [2, 15, 11, 7]
target = 9

def two_sum(target, array):
    #Make a list that stores numbers and their indices
    num_dict = {}

    #iterate through the given array
    for i, num in enumerate(array):
        #calculate the complement
        complement =  target - num
        
        #Check if the complement is in the hash table
        if complement in num_dict:
            #if the complement is in the dictionary return both indices
            return [num_dict[complement], i]
        #if not found add the current number to the hash table
        num_dict[num] = i

    #if no solution is found return empty list
    return[]


print(two_sum(target, nums))