# The body mass index​ (BMI) is a number that can be calculated for any individual by using the equation
# BMI = 703w / h**2
# where weight​ (w) is in pounds and height​ (h) is in inches.  Use this information to complete the following.

from sympy import symbols, solve, pprint, Derivative
import math

# rounding

dec_places = 0

# input variables

weight = 219
height = 6.2
target_bmi = 24.9

height = int( height ) * 12 + ( height % 1 * 10 )

w, h = symbols( 'w, h' )

fBMI = 703*w / h**2

w_bmi = fBMI.subs( { h: height } )
bmi = w_bmi.subs( { w: weight } )

print( 'raw bmi: {0}'.format( bmi ) )

target_weight = solve( w_bmi - target_bmi, w )[ 0 ]

# a
# Calculate the BMI for a person who weighs 219 pounds and is 6 prime 2 double prime tall.
print( 'A person that weighs {0}lbs and is {1}in tall has a BMI of {2}'.format( weight, height, round( bmi, dec_places ) ) )
# b
# How much weight would the person in part a have to lose to reach a BMI of 24.9​?
print( 'They would need to loose {0}lbs to reach a BMI of {1}'.format( round( weight - target_weight, dec_places ), target_bmi ) )

# c
# For a 126​-lb. ​female, what is the rate of change of BMI with respect to​ height?

weight = 126
dH = Derivative( fBMI.subs( { w: weight } ) ).doit()
pprint( dH )

# d
# Calculate f'( 66 ).
height = 66
rate_of_change = float( dH.subs( { h: height } ) )

print( 'rate of change for female {0}'.format( round( rate_of_change, 2 ) ) )