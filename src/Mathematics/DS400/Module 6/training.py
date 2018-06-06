# A company found that new employees prefer training sessions of moderate​ length; shorter training sessions provided too little instruction to complete a​ task,
# while longer training sessions contain too much instruction to remember. 
# For a training session on a particular​ task, the company determined that the ratings new employees gave for the training session could be approximated by 

# R(t) = 34*t / t ^2 + 289

from sympy import solve, Limit, lambdify, symbols, diff, ln
import matplotlib.pyplot as plt
import numpy as np

g_xlim = [ 0, 40 ]
g_ylim = [ 0, 7 ]

t = symbols( 't' )
T = 34 * t /  ( t ** 2 + 289 )
dT = diff( T, t )

lam_x = lambdify( t, T, modules=['numpy'] )

x_vals = np.linspace( g_xlim[ 0 ], g_xlim[ 1 ], 1000, endpoint = True )
y_vals = lam_x( x_vals )

plt.plot( x_vals, y_vals )

critical_numbers = solve( dT, t )

raiting = max( critical_numbers )

plt.vlines( x= raiting, ymin=0, ymax = max( y_vals ), color='red', zorder=2)
plt.text( raiting, 1.5, 'Highest Rating: {0}'.format( raiting ) )

plt.xlim( g_xlim )
plt.ylim( g_ylim )
plt.xlabel( 'Length' )
plt.ylabel( 'Rating' )
plt.show()