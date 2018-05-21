# MSDS 400 Module 8 Practice 2
'''
Section 6.5 of "Think Python" shows the following factorial function.
Note that the variable "result" is local to the functions which use it.

Compare these functions to the definitions in Lial.
'''


def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n - 1)
        result = n * recurse
        return result


def perm(n, k):
    if n == 0:
        return 1
    if k > n:
        return -1
    else:
        return (factorial(n)) / factorial(n - k)


def comb(n, k):
    result = perm(n, k)
    result = result / factorial(k)
    result = int(result)
    return result


# Section 5.11 of "Think Python" 2nd edition or pages 55-56 of the 3rd edition
# presents keyboard input.  Enter the number in the interpreter and hit enter.
# Keyboard input will be used for a factorial calculation in the next section.

print('Enter a positive integer to obtain the factorial value.')
print('Enter a negative integer to stop.')
print('In either case, hit enter or the code will not work.')

# The statement input() accepts keyboard input and produces a string which
# must be converted to a numeric variable for further calculations.

inp = input()
int_inp = int(inp)

if int_inp > 0:
    fact_of_inp = factorial(int_inp)
    print('Factorial of {} is equal to {}'.format(int_inp, fact_of_inp))
else:
    print('No calculation.\n')

# Example calculations follow.

permutation = perm(10, 5)
print('Permutation of 10 elements taken 5 at a time ={}'.format(permutation))

combination = comb(10, 5)
print('Combination of 10 elements taken 5 at a time = {}'.format(combination))

import matplotlib.pyplot as plt

'''
An example of code for calculating a binomial probability follows
Section 5.11 of "Think Python" presents keyboard input.
Keyboard input will be used for a binomial calculation.

In the code which follows, note the type conversions from string to
integer, integer to floating point and back.
'''
print('In each instance, hit enter after submitting the requested number.')
print('Enter a positive integer for the number of repeated trials.')

inp = input()
int_inp = int(inp)  # This converts n from a string to an integer.

print('Enter the number of successes.')
success = input()
int_success_int = int(success)

print('Enter the probability of success.')
prob_of_s = input()
int_prob_of_s = float(prob_of_s)  # This converts p from a string to a floating point number.

prob = (comb(int_inp, int_success_int)) *\
       (int_prob_of_s ** int_success_int) * \
       ((1.0 - int_prob_of_s) ** (int_inp - int_success_int))
print('Binomial probability with n = {}, k= {}, p= {} is {}\n'.format(int_inp, int_success_int, int_prob_of_s, prob))
'''
The following example shows how to calculate a binomial distribution
and print the result.  First a binomial function will be defined.  The
values previously entered for the number of repeated trials, the
number of successes and the probability of success will be used.
'''


def binomial(n, k, p):
    return (comb(n, k)) * (p ** k) * ((1.0 - p) ** (n - k))


print('Binomial distribution with {} trials and p={} follows.\n'.format(int_inp, int_prob_of_s))
distribution = []
for i in range(0, int_inp + 1):
    prob = binomial(int_inp, i, int_prob_of_s)
    print('# of successes = {} probability = {:2.2f}'.format(i, prob))
    distribution = distribution + [prob]

x = range(0, int_inp + 1, 1)  # x and y are both lists with the same number of elements.
y = distribution
'''
The plot is produced in layers.  bar() places the red bars of width 0.4
centered on x values. The heigth is determined by y.  The plot()
statement places the line plot on the chart.  With only one show()
statement, the figure() statement is unnecessary.
'''
plt.bar(x, y, width=0.4, align='center', color='r')
plt.plot(x, y)
plt.xlabel('Total Number of Trials')
plt.ylabel('Probability of Success')
plt.title('Binomial Probabilities ')
plt.show()

# Exercise 1: Using the functions as defined in the code check the calculations
# in Lial Section 8.1 Examples 3 and 9, and Section 8.2 Example 3.

# Exercise 2: Using the concept of a "for" loop discussed in Section 10.3
# of "Think Python", write a function that calculates factorials without
# using a recursive approach.

# Exercise 3: Using a variation of the code and functions defined,
# check the calculations in Lial Section 8.4 Examples 2 and 3.
# Note the distributions which are produced.

# Exercise 4: Using the function "binomial" as defined in the code, write
# the code to verify the calculatons in Lial Section 8.5 Example 7.