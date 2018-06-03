# A toilet manufacturer has decided to come out with a new and improved toilet. 
# The fixed cost for the production of this new toilet line is​ $16,600 and the variable costs are $ 68 per toilet. 
# The company expects to sell the toilets for $ 159. 
# 
# Formulate a function​ C(x) for the total cost of producing x new toilets and a function​ R(x) for the total revenue generated from the sales of x toilets.

from sympy import ( symbols )

x = symbols( 'x', positive = True )
C = x + 16600
R = 159*x