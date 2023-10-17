##########################################
#   Author: Niclas Alexander Pedersen    #
# Challenge: Pascal's triangle Leetcode  #
#           Written: 08/09/23            #
#            Language: Python            #
#                                        #
##########################################

numRows = 10**8

def pascals_triangle(numRows):
    #Every triangle starts with a 1
    Output = [[1]]

    #Iterates for every number of rows 
    for i in range(1, numRows):
        #Acesses the last iteration in the row by calling -1
        prev_row = Output[-1] 
        #Rows always starts with 1
        new_row = [1]

        #Iterates over the new row and finds the k'th elements 
        for j in range(1, i):
            #The new element is whatever is in the previos row above summed
            new_element = prev_row[j - 1] + prev_row[j]
            #Adds new element to our new row array 
            new_row.append(new_element)

        #All rows always ends with a 1
        new_row.append(1)
        #Adds new row to the overall triangle
        Output.append(new_row)

    return Output

print(pascals_triangle(numRows))