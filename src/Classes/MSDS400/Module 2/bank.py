# A bank has set aside a maximum of ​$30 million for commercial and home loans. 
# Every million dollars in commercial loans requires 2 application forms while every million dollars in home loans requires 3 forms. 
# The bank cannot process more than 84 forms at this time. 
# The​ bank's policy is to loan at least four times as much for home loans as for commercial loans. 
# At least​ $10 million will be used for these two types of loans. 
# The bank earns 10​% on commercial loans and 12​% on home loans. 
# What amount of money should be allotted for each type of loan to maximize the interest​ income?

from pulp import *

bank_lending = LpProblem( "Bank Lending Problem", LpMaximize )

x1 = LpVariable( "x1", 0 )
x2 = LpVariable( "x2", 0 )

w = LpVariable( "w" )

bank_lending +=  .10*x1 + .12*x2

# Constraints

bank_lending += x1 + x2 <= 30
bank_lending += x1 + x2 >= 10

bank_lending += 2*x1 + 3*x2 <= 84
bank_lending += 4*x1 <= x2

bank_lending.solve()
bank_lending.LpStatus[bank_lending.status]

for variable in bank_lending.variables():
    print("{0} = {1}".format(variable.name, variable.varValue))

print( 'Optimal Sln: {0}'.format(pulp.value(bank_lending.objective)))