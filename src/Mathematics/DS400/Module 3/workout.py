# As part of a weight reduction​ program, a man designs a monthly exercise program consisting of​ bicycling, jogging, and swimming.

# He would like to 
# exercise at most 28 ​hours, 
# devote at most 6 hours to​ swimming, 
# and jog for no more than the total number of hours bicycling and swimming.

# The calories burned by this person per hour by​ bicycling, jogging, and swimming are​ 200, 427​, and 283​, respectively. 

# How many hours should be allotted to each activity to maximize the number of calories​ burned? What is the maximum number of calories he will​ burn?
#  (Hint: Write the constraint involving jogging in the form less than or equals​ 0.)

# Let x 1 be the number of hours spent​ bicycling, 
# let x 2 be the number of hours spent​ jogging, 
# and let x 3 be the number of hours spent swimming. 
# 
# What is the objective​ function?

from pulp import *

workout = LpProblem( "Workout Problem", LpMaximize )

x1 = LpVariable( "x1", 0 ) # Bicycling
x2 = LpVariable( "x2", 0 ) # Jogging
x3 = LpVariable( "x3", 0 ) # Swimming

w = LpVariable( "w" )

workout += 200*x1 + 427*x2 + 283*x3

# Constraints

workout += x1 + x2 + x3 <= 28 # no more than total hours
workout += x3 <= 6 # at most hours swimming
workout += x2 <= x1 + x3 # jog no more than Bicycling + Swimming


workout.solve()
workout.LpStatus[ workout.status ]

for variable in workout.variables():
    print("{0} = {1}".format( variable.name, variable.varValue ))

print( 'Optimal Sln: {0}'.format(pulp.value( workout.objective )))