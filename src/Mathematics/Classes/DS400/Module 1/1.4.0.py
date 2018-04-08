import numpy 
from numpy import array, absolute

t= [1, 2, 3]
print ('\nValue at first location:', t[0])
print ('Value at third location:', t[2])
print ('Value located using negative index:', t[-2])

print ('Comparison of a concatenated list with an array ')
r= [4, 5, 6]
print ('r=', r) 
print ('t=', t )
result1= t + r
print ('Concatenation example using t and r lists.', result1)
result2=array([t,r])
print ('\nComparison of concatenation with array([t,r]).')
print (result2)

# Note the different results produced by indexing for a list and an array.
print ('\nThe second element of the preceding list and array')
print (result1[1])
print (result2[1])

print ('\nSlicing to produce an element, a column and a row of the array')
print (result2[0,1])
print (result2[:,1])  # Note the horizontal output of a column.
print (result2[1,:])

print ('\nExample 1 Section 2.3 Lial showing array addition from page 72.')
m= array([[10,12,5],[15, 20, 8]])
n= array([[45, 35, 20],[65, 40, 35]])
q= m + n
print ('\nArrays in order: m , n and m+n')
print (m) 
print ('\n', n)   # Note that context determines the purpose of "n".
print ('\n', q) 

print ('\nSubtraction of n from m equals q')
q= m - n
print (q)

s= 2.0
print ('\nMultiplication of q by a scalar', s)
q= s*q
print (q)

print ('\nFunctions can be applied to an array such as absolute value')
q= absolute(q)
print (q)