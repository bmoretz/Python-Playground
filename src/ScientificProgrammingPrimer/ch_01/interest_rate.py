# Let p be a bank’s interest rate in percent per year. 
# An initial amount A has then grown to A ( 1  +  p/100)^ n after n years. 
# Make a program for computing how much money 1000 euros have grown to after three years with 5 percent interest rate.

A = 1000
N = 5.0
p = 0.05

def R( amount, rate, time ):
	return amount * ( 1 + rate/100 ) ** time

R( A, N, p )