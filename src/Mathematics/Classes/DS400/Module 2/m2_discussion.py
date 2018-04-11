import pulp

hedge_model = pulp.LpProblem( "LP Heding Problem", pulp.LpMaximize )

# risk > 0
r = pulp.LpVariable( 'r', lowBound = 1 )

# hedge > 0
h = pulp.LpVariable( 'h', lowBound = 1 )

# P = r + h
hedge_model += r + h, "Objective"

# must be at least 2 units of hedge per 3 units of risk.
hedge_model += 3*r <= 2*r

# total invested units <= 100
hedge_model += r + h <= 100

# must be at lest 40 units of security risk.
hedge_model += r >= 40

hedge_model

hedge_model.solve()
pulp.LpStatus[hedge_model.status]

for variable in hedge_model.variables():
    print("{0} = {1}".format(variable.name, variable.varValue))

print( 'Optimal Capital Investment: {0}'.format(pulp.value(hedge_model.objective)))