# A toy making company has at least 
# 
#	300 squares of​ felt, 
#	700 oz of​ stuffing, and 
#	230 ft of trim to make dogs and dinosaurs.

# A dog uses ( $1.25 )
#	1 square of​ felt, 
#	4 oz of​ stuffing, and 
#	1 ft of trim. 
# 
# A dinosaur uses ( $1.89 ) 
#	2 squares of​ felt, 
#	3 oz of​ stuffing, and 
#	1 ft of trim.

# It costs the company ​$1.25 to make each dog and ​$1.89 for each dinosaur. 
# What is the​ company's minimum​ cost?

import numpy as np
from numpy import matrix, transpose, dot

dog_cost, dinosaur_cost = 1.25, 1.89

n_felt = 300

n_stuff = 700
n_trim = 230

felt = [ 1, 2 ]
stuff = [ 4, 3 ]
trim = [ 1, 1 ]

# Set up the constraints and obtain the corner points
a1 = np.array( [ felt, stuff ] )
b1 = np.array( [ n_felt, n_stuff ] )

# solve the two sets of equations at a time to get points of intersection of the lines
c1 = np.linalg.solve( a1, b1 )
print( c1 )

# Second pair of corner points
a2 = np.array( [ felt, trim ] )
b2 = np.array( [ n_felt, n_trim ] )
c2 = np.linalg.solve( a2, b2 )

print( c2 )

# Third pair of corner points
a3 = np.array( [ stuff, trim ] )
b3 = np.array( [ n_stuff, n_trim ] )
c3 = np.linalg.solve( a3, b3 )

print( c3 )

# Use the corner points and compute dot product to determine the minimum value 
x= [ c1[ 0 ], c2[ 0 ], c3[ 0 ] ]
y= [ c1[ 1 ], c2[ 1 ], c3[ 1 ] ]

obj= matrix( [ dog_cost, dinosaur_cost ] )
obj= transpose( obj )
corners= matrix( [x,y] )
corners= transpose( corners )
result= dot( corners,obj )

print ("Value of Objective Function at Each Corner Point", result)
print ("Minimum cost of the company is ", result.min() )