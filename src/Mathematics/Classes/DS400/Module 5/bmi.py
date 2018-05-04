# The body mass index​ (BMI) is a number that can be calculated for any individual by using the equation
# BMI = 703w / h**2
# where weight​ (w) is in pounds and height​ (h) is in inches.  Use this information to complete the following.

from sympy import symbols, solve

weight = 219
height = 6.2

target_weight = 24.8

height = height * 12
w, h = symbols( 'w, h' )
fBMI = 703*w / h**2
bmi = fBMI.subs( { w: weight, h: height } )

print( 'Person that weighs {0}lbs and is {1}in tall has a BMI of {2}'.format( weight, height, bmi ) )

solve( fBMI, w, dict = True )

pprint( w_bmi )