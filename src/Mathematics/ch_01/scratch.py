# Exponents

2 ** 10

8 ** ( 1/3 )

# Fractions

from fractions import Fraction

f = Fraction( 3, 4 )

f

r = Fraction( 3, 4 ) + 1 + 1.5

print( r )

r = Fraction( 3, 4 ) + 1 + Fraction( 1 / 4 )

r

a = 2 + 3j

type( a )

a = complex( 2, 3 )

a

b = 3 + 3j

a + b

a -  b

a * b

a / b

# real - img

z = 2 + 3j

z.real
z.imag

z.conjugate()

( z.real ** 2 + z.imag ** 2 ) ** 0.5

abs( 5 )
abs( -5 )

abs( z )

a = input()

a

s1 = 'a string'
s2 = "a string"

a = 1

int( a ) + 1

float( a ) + 2

int( "2.5" )

int( '2.5' )

a = float( input() )

try:

	a = float( input('Enter a number: ') )
	print( a )
except ValueError:
	print( 'You entered an invalid number' )


1.1.is_integer()
1.0.is_integer()

try:
	a = Fraction( input( 'Enter a fraction: ' ) )
except ZeroDivisionError:
	print( 'Invalid Fraction' )

try:
	a = complex( input( 'Enter a complex number: ' ) )
except ValueError:
	print( 'Invalid Fraction' )

def is_factor( a, b ) :
	if b % a == 0:
		return True
	else:
		return False

is_factor( 4, 1024 )

for i in range( 1, 4 ):
	print( i )

for i in range( 1, 10, 2 ):
	print( i )

