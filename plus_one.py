##########################################
#   Author: Niclas Alexander Pedersen    #
#      Challenge: Plus one Leetcode      #
#           Written: 08/09/23            #
#            Language: Python            #
#                                        #
##########################################

digits = [9,9,9]


def plus_one(digits):
    #Creates output array
    Output = []

    #Combines the integer in the by multiplying with the corresponding power of 10 and then adds them together
    total = sum(d * 10**i for i, d in enumerate(digits[::-1]))

    #Increments the total with 1
    total += 1

    #Splits the number into digits and appends the output array with these
    for i in str(total):
        Output.append(i)

    return Output

print(plus_one(digits))