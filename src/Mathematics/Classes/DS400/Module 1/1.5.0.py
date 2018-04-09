import numpy 
from numpy import *
from numpy.linalg import *

rhs= [96, 87, 74]
rhs=matrix(rhs)
rhs=transpose(rhs)
print ('\nRight Hand Side of Equation')
print (rhs)

A =[[1, 3, 4], [2, 1, 3], [4, 2, 1]]
A= matrix(A)
print ('\nMatrix A')
print (A)

IA= inv(A)
IA

I= dot(IA,A)
I= int_(I)               # This converts floating point to integer.
I

result = dot(IA,rhs)
result = int_(result)    # This converts floating point to integer.
result

result2= linalg.solve(A,rhs)
int_(result2)   # This converts floating point to integer.

A= [[1,2,3],[-3,-2,-1], [-1,0,1]]
A= array(A)
IA= inv(A)
IA

