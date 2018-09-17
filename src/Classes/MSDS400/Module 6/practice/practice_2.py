
# MSDS 400 Module 6 Practice 2

import matplotlib.pyplot as plt
from numpy import poly1d, linspace

'''
The first example shows how to generate and print a second degree
polynomial with coefficients, 1, -2 and 4.  The software is not limited
to second degree polynomials.  Higher order can be generated.  The critical
thing is to have all the coefficients in the right sequence.
'''
p = poly1d([5, -3, 2])
print('Second Degree Polynomial')
print(p)

# Now a fourth degree polynomial will be generated and printed.

q = poly1d([2, 1, 4, -2, 3])
print('\nFourth Degree Polynomial')
print(q)

# It is possible to combine p and q algebraically.

print('\nCombination')
g = p + p*q
print(g)

# Derivatives of different orders may be calculated.  This next section will
# show determination of the first and second derivatives of p.

print('\nFirst Derivative')
h = p.deriv(m=1)  # First derivative with m=1.
print(h)
print(h.roots)

print('\nSecond Derivative')
t = p.deriv(m=2)  # Second derivative with m=2.
print(t)
print(t.roots)

'''
Using t, the original function p can be restored if the missing
coefficients -2 and 4 are supplied.  Different coefficients would result
in a different function instead of the original p.
'''
print('\nIntegrated Derivative')
w = t.integ(m=2, k=[-3, 2])
print(w)
print(w.coeffs)

print('\nrandom stuff below')
new = t.integ(m=2, k=[-2, 4])
print(new)
print(new.deriv(m=1))

# Roots may also be found.  This is useful when locating the maxima, minima
# and inflection points of a function from the first and second derivatives.

print('\nRoots of polynomial')
print(w.roots)

'''
Plotting requires defining a domain for the polynomial.  The linspace
function is used to set boundaries and define the number of points
used for calculation. A new polynomial p will be defined.
'''
p = poly1d([.3333, 0, -1, 5])

# As a final example, we will find the first and second derivatives of the
# polynomial p, find the roots of the derivatives and plot the functions.

g = p.deriv(m=1)

print('\nRoots of First Derivative')
print(g.roots)

print('\nRoots of Second Derivative')
q = p.deriv(m=2)
print(q.roots)

x = linspace(-4, 4, 101)
y = p(x)
yg = g(x)  # These statements define points for plotting.
yq = q(x)
y0 = 0*x   # This statement defines the y axis for plotting.

# What is shown below is a different way to legends using a label.  Python
# will pick the colors to assign to the labels and the plotted points.

plt.plot(x, y, label='y=p(x)')
plt.plot(x, yg, label='First Derivative')
plt.plot(x, yq, label='Second Derivative')
plt.legend(loc='best')

plt.plot(x, y0)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Plot Showing Function, First and Second Derivatives')
plt.show()

# Exercise: Refer to Lial Section 14.1 Example 2.  Duplicate the results
# showing plots of the function and derivatives.  Compare to the answer sheet.

plt.figure()
p = poly1d([3, -4, -12, 0, 2])
print('\nFourth Degree Polynomial')
print(p)
print('\nFirst Derivative')
g = p.deriv(m=1)  # First derivative with m=1.
print(g)
print('\nSecond Derivative')
q = p.deriv(m=2)  # Second derivative with m=2.
print(q)
x = linspace(-2, 3, 101)
y = p(x)
yg = g(x)  # These statements define points for plotting.
yq = q(x)
y0 = 0*x  # This statement defines the y axis for plotting.
plt.plot(x, y, label='y=p(x)')
plt.plot(x, yg, label='First Derivative')
plt.plot(x, yq, label='Second Derivative')
plt.legend(loc='best')

plt.plot(x, y0)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Plot Showing Function, First and Second Derivatives')
plt.show()