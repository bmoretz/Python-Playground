from sympy import FiniteSet

O = FiniteSet( 'a', 'p', 'e', 's', 'o' )
S = FiniteSet( 'h', 'o', 'c', 'a', 'b' )
H = FiniteSet( 'h', 'b', 'd', 'm', 't' )

U = O.union( H ).union( S )

sh = S.union( H )

sh.complement( U )