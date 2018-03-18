from matplotlib import pyplot as plt
from sympy import Limit, Symbol, S
import numpy as np

def f(x):
    return 1/x

fx_name = r'$f(x)=\frac{1}{x}$'
# using 101 steps results in in array including the value 0
x = np.linspace(-10,10,101)
# f(0) = nan -> a nan value creates a gap
y = f(x)
plt.plot(x, y, label=fx_name)
plt.legend(loc='upper left')
plt.show()

# Limit

x = Symbol( 'x' )
# lim x -> +inf
l = Limit( '1/x', x, S.Infinity )
l.doit()

# lim x -> 0, from -inf
l = Limit( '1/x', x, 0, dir='-' )
l.doit()

# lim x -> 0, from +inf
l = Limit( '1/x', x, 0, dir='+' )
l.doit()