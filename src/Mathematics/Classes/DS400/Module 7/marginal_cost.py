# Find the cost function from the marginal cost function.

from sympy import solve, symbols, lambdify, diff, Integral, exp, pprint, pretty, simplify
import matplotlib.pyplot as plt
import numpy as np

x = symbols( 'x' )
mC = 0.02 * exp( 0.05*x )
fixed_cost = 9

C = Integral( mC, x ).doit()

# Note, this doesn't subtract the constant K from the fixed cost
simplify( C.evalf() - fixed_cost )