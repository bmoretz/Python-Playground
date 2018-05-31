from sympy import FiniteSet

O = FiniteSet( 'b', 'o', 'h', 't', 'p' )
H = FiniteSet( 's', 'p', 'c', 'b', 'e' )
S = FiniteSet( 'd', 's', 'm', 'e', 'a' )

U = O.union( H ).union( S )

ho = H.union( O )

ho.complement( U )