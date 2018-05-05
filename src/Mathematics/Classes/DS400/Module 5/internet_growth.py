# The growth in the number​ (in millions) of Internet users in a certain country between 1990 and 2015 can be approximated by a logistic function with 
# k = 0.0013​, 
# where t is the number of years since 1990. 
# In 1990​ (when t = ​0), the number of users was about 4 ​million, and the number is expected to level out around 210 million.

from sympy import *
from fractions import Fraction

init_printing()

def disp_fun( f ):
	pprint( '\n{0}\n\n'.format( pretty( f ) ) )

# Find the growth function​ G(t) for the number of Internet users in the country.

cK = 0.0015
start_year = 1990
growth_0 = 2
growth_exp = 230

dec_places = 1

# Growth Function

k, t, g0, m = symbols( 'k, t, g0, m' )
G = m*g0 / ( g0 + ( m - g0 ) * exp( -k*m*t ) ) 
dG = Derivative( G, t ).doit()

def users_at_year( year ):
	u_year = G.subs( { g0: growth_0, m: growth_exp, k: cK, t: year - 1990 } )
	return round( u_year, dec_places )

def growth_at_year( year ):
	g_year = dG.subs( { g0: growth_0, m: growth_exp, k: cK, t: year - 1990 } )
	return round( g_year, dec_places )

gI = G.subs( { g0: growth_0, m: growth_exp, k: cK } )

gI

disp_fun( simplify( gI ) )
dGI = Derivative( gI, t ).doit()

disp_fun( dGI )
disp_fun( simplify( dGI ) )

users_at_year( 2009 )

growth_at_year( 2009 )

228/2

460/2