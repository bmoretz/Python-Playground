# MSDS 400 Module 9 Practice 1

from numpy import random, arange, array
import matplotlib.pyplot as plt


# The random sample size=nsamples and can be specified by the student.

nsamples = 100
sample = random.random(nsamples)  # This draws a random sample.

nbins = 10  # This defines the number of subintervals for the histogram.
bns = float(nbins)
'''
For a uniform distribution, the proportions in each subinterval are
expected to be the same.  With ten subintervals, this amounts to 0.1 in
each.  With 20 subintervals it amounts to 0.05.
'''
expected = 1.0 / bns  # This defines the expected subinterval proportion.

ind = arange(nbins)  # This sets ind to serve as a range of indices.
h = [0] * nbins  # This prepares h to serve as a list of the proper length.
histogram = {}  # This defines histogram as a void dictionary.

for k in ind:
    histogram[k] = 0  # This initializes the dictionary with zero counts.
'''
In the for loop we run v across all randomly generated values and categorize
them according to which bin they fall in.  The count for each bin is
accumulated in the dictionary histogram[] indexed according to ind[].
'''
for v in sample:
    for k in ind:
        xk = float(k)
        if xk / bns <= v < (xk + 1) / bns:
            histogram[k] += 1
'''
The following for loop converts each count to a proportion and stores the
proportions in the list h[] and the dictionary histogram[].  The list h[]
will be used for plotting and the dictionary histogram[] for computing.
'''
for k in ind:
    x = histogram[k]
    x = x / float(nsamples)
    h[k] = [x]
    histogram[k] = x
'''
Measuring the degree of convergence of the histogram to the limiting uniform
distribution can be done in various ways.  Here we use the sum of absolute
differences between the expected proportion and the observed proportion.
'''
total = 0.0
for k in ind:
    total = total + abs(expected - histogram[k])
total = format(total, '0.4e')
print('Sum of Absolute Differences= {}'.format(total))

h = array(h)
cell = ind + 0.5  # This will center the bar in the middle of the subinterval.

plt.bar(cell, h, width=0.5, align='center', color='r')
plt.plot(cell, h)

# The following statements are used to form the title for the plot.
# Note how computational information is being included in the title.

string = str(nsamples) + '   Absolute Difference= ' + str(sum)
plt.title('Histogram   n=' + string)

plt.ylabel('Proportions')
plt.xlabel('Subintervals')
plt.show()

# Exercise 1:  Generate a series of plotted histograms using the code.
# Generate five plots using nsample values increasing by powers of ten:  100,
# 1000, 10000, 100000, 1000000.  Calculate the sample mean value and absolute
# difference for each plot.  Evaluate the changes in absoute difference and
# mean values as the sample size increases.  When computing the sample mean
# value, use the dictionary histogram[] and the ind array. The ind array needs
# to be centered within each subinterval. (Hint: add 0.5)

# Exercise 2:  Add code to estimate the sample variance for each random sample.
# For simplicity, calculate the sum of the following terms:
# histogram[k]*(ind[k]-mean)**2.  In the limit as nsamples approaches
# infinity, for sample data grouped in subintervals centered at 0.5, 1.5, ...,
# 8.5, 9.5, the limiting value is 8.25.  Do you see convergence?

