from sympy import symbols, solve, diff, pprint, integrate
# The 2000 census in a particular area gives us an age distribution that is approximately given​ (in millions) by the function

multiplier = 1000000

x = symbols( 'x' )
F = 39 + 2.11*x - 0.81*x**2

# where x varies from 0 to 9 decades. 
# The population of a given age group can be found by integrating this function over the interval for that age group.

# Find the integral over the interval
a, b = 0, 9
population = round( integrate( F, ( x, a, b ) ) )

# b
print( 'The total number of people in this area aged 0 to 90 was about {0} million in 2000.'.format( population ) )

# Find the number of people alive in 2000 that were born in the seventies​, that​ is, those in the range of 4 to 5 decades in 2000
a, b = 4, 5
round( integrate( F, ( x, a, b ) ) )