from sympy import Matrix
import numpy as np

A = Matrix( [[3, 4], \
			 [2, 1 ]] ) 

B = Matrix( [[-1, 0, 1, 2], \
			 [4, 3,2, 1 ]] ) 

C = Matrix( [[-2, 3, 0], \
			 [2, -2, 1]] )

# a
A.transpose()

# b
C.transpose()

# c
A*A

# d
A*B

# e
A*C

# f
B*A # doesn't exist

# g
C.transpose() * A

# h
A.det()

# i
B.det()

# j
C.det()

# k
A.transpose().det()

# m
A.trace()

# n
A.transpose().trace()


