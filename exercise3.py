#!/usr/bin/env python


##################
# special topic exercise 3
# working with functionss
##################

# Write a function in python called sum_it that takes 2 numbers and returns the 
# sum of them.
# ie
a = sum_it(2,4)
print a
6

# Now modify the function so that it will sum the two numbers unless
# they are the same, in which case it will multiply them together
# ie use if else statments in the function.
b = sum_it(4,4)
print b
16
c = sum_it(3,2)
print c
5

# Question: Are variables local to the function (ie used inside the function)
# available to the main script? Show how this works with an example.



# Write another function called sum_string that takes two string numbers
# and then returns the sum of the numbers (as a string) repressented by 
# the strings.** Get this function to call the sum_it function**. 
result = sum_string("3", "6")
print result
"9"

