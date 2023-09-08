##########################################
#   Author: Niclas Alexander Pedersen    #
#      Challenge: FizzBuzz Leetcode      #
#           Written: 08/09/23            #
#            Language: Python            #
##########################################

#Solution 1 with list comprehension

[print("Fizz"*(i%3==0)+"Buzz"*(i%5==0) or i)for i in range(1, 101)]

#Solution 2 done more tradionally with a function can be expanded with more words and divisors

def fizzbuzz(n, divisors, words):
    assert(len(divisors) == len(words))
    for i in range(1, n+1):
        s = ""
        for j, d in enumerate(divisors):
            if i % d == 0:
                s += words[j]
        if s == "":
            s = i
        print(s)

divisors = [3, 5, 8]
words = ["Fizz", "Buzz", "Kizz"]

fizzbuzz(1000, divisors, words)