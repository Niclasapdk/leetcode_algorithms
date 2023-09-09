##########################################
#   Author: Niclas Alexander Pedersen    #
#      Challenge: sqrt(x) Leetcode       #
#           Written: 09/09/23            #
#            Language: Python            #
##########################################

#Sqrt root function implemented in python using the numerical approximation of newton raphson 

def sqrt(x, epsilon = 1e-6):
    #initial guess for the square root
    guess = x / 2.0

    while abs(guess * guess - x) > epsilon:
        #Use newton raphson to update the guess 
        guess = 0.5 * (guess + x / guess)
    #rounds down to the nearest integer as described in the assignment
    return int(guess)

x = 8 
print(sqrt(x))