# The table below gives the proportion of children in a certain country in a year who are living in a family in each income​ group, 
# as well as the proportion who are living with two married parents in each income group. 

pF1, pEF1 = 0.148, 0.161
pF2, pEF2 = 0.156, 0.313
pF3, pEF3 = 0.174, 0.537
pF4, pEF4 = 0.179, 0.772
pF5, pEF5 = 0.129, 0.831
pF6, pEF6 = 0.214, 0.944

pF = pF1 * pEF1

probability = pF / ( ( pF1 * pEF1 ) + ( pF2 * pEF2 ) + ( pF3 * pEF3 ) + ( pF4 * pEF4 ) + ( pF5 * pEF5 ) + ( pF6 * pEF6 ) )

round( probability, 3 )