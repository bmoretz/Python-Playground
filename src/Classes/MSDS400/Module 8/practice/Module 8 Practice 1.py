# MSDS 400 Module 8 Practice 1

'''
Instructions---The module is self contained.
The data for the following example are taken from Lial Shapter 7 Example 5.
Various set operations will be performed.  The first steps are to define the
lists of data which will then be converted into set objects.  Various set
operations will be demonstrated.  Finally, a set will be converted to a list.
'''

# set([1, 2, 3]) is the same as {1, 2, 3}. The former is easier to read, but the later is about twice as fast for the CPU.
U = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
A = {1, 2, 4, 5, 7}
B = {2, 4, 5, 7, 9, 11}
'''
The following generates new variables only to facilitate printing.
The variables Uab, AB, Ac, Bc, AsB, R, Add, Addc and SD are for my
convenience only.  The important thing is to study the set operations.
'''

# Example of union operation
Uab = A | B
print('\nUnion of A and B =', Uab, ' \n')

# Example of intersection operation
AB = A & B
print('Intersection of A and B =', AB, '\n')

# Example of finding the complement of A and B
Ac = U - A
Bc = U - B
print('A complement =', Ac)
print('B complement =', Bc, '\n')

# Example of finding the symmetric difference of A and b
# The symmetric difference are elements in A and B not common to both
AsB = A ^ B
print('Symmetric difference of A and B = ', AsB)

# Example showing another way to obtain the symmetric difference
SD = (A | B) - (A & B)
print('Symmetric difference by union and intersection =', SD, '\n')

# Union of several sets
R = Ac | Bc | AB
print('Union of Ac, Bc and AB  ', R)
print('Original set U was ', U)

# Items can be added to sets using the union operation
Add = {12, 13, 14}
U = U | Add
print(U)
print('Updated version of U = ', U, '\n')
print(Add)
# Removal is possible using the complement operation
Addc = U - Add
print(U)
print(Add)
U = U & Addc
print(U)
print('Original version of U =', U, '\n')

# Following these operations, a set may be converted to a list.
U = list(U)
print('U is now a list.', U)

'''
Generate the universe U.  Note that range(1,27,1) will be used to produce
a list of 26 positive integers for set operations.  Remember, range()
includes the first, i.e. 1, but not the last element, i.e. 27.  The third
argument, 1, defines the step used between consecutive elements.  Note that
the functions used in this module are available from Python itself.
'''

U = range(1, 27)
'''
Slice the list U into three subsets.  Note that slicing is inclusive of the
first indexed element and exclusive of the last indexed element.  Also, the
first element has 0 for an index.
'''
A = U[0:13]
B = U[13:]
C = U[7:20]

A = set(A)
B = set(B)
C = set(C)
U = set(U)
print('The universe U is', U)

print('\n A is', A)  # Compare these sets to the slice statements above.
print('B is', B)
print('C is', C)
'''
It is assumed in this module that each element of U occurs with equal
probability as would be the case with random sampling with replacement.
This assumption allows the probability of a set to be calculated as the
ratio of the length of the set (i.e. number of elements) divided by the
overall length of U which in this Module is 26.  Note that %r and %s both
can be used with strings and lists.

Convert the length of T to floating point to avoid interger division.
The function round() was defined in earlier modules as was float().
'''
T = float(len(U))

# Demonstrate the null intersection and probability.
Null = A & B
print('Probability of null intersection ', round((len(Null)/T), 3))

# Demonstrate the Union Rule for Probability.
print('Intersection of A and C is ', (A & C))
print('Union of A and C ', (A | C), '\n')

P = (len(A) + len(C) - len(A & C))
print('Probability of A union C = ', round((len(A | C)/T), 3), '\n')
print('Result of Union Rule Summation =', ((P/T), 3), '\n')

# Demonstrate the calculation of Odds using the complement rule.

print('Complement of C is', (U-C))
print('Odds of C are', round((len(C)/float(len(U-C))), 3), '\n')

print('Complement of A intersection C is', U-(A & C))
P = (len(A & C)/float(len(U-(A & C))))
print('Odds of A intersection C are', round(P, 3), '\n')

# Demonstrate conditional probability.
P = round(len(A & C)/float(len(C)), 3)
print('Conditional probability of A given C is', P)

# Demonstrate the product rule.
print('Probability of A and C intersection is', round((len(A & C)/T), 3))
Q = len(C)/T
print('Probability of C is', round(Q, 3))
print('Product rule result for A and C intersection is', round(P*Q, 3))


# Exercise 1: Duplicate Examples 6 and 7 from Lial Section 7.1.
# Compare your code to the answer sheet.

# Exercise 2:  Refer to Section 7.6 of Lial.  Using the sets defined above and
# set operations apply Bayes' Theorem.  Calculate the conditional
# probability of A given C, and the probability of C given A.
