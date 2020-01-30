"""
@AnilC
Top Brass Problem
"""
from pulp import *

f = LpVariable("f",0,1000)
s = LpVariable("s",0,1500)

tb1 = LpProblem("topBrass", LpMaximize)
tb1 += f + s <= 1750		#add constraint
tb1 += 4*f + 2*s <= 4800	#add constraint
tb1 += 12*f + 9*s 			#add objective
status = tb1.solve()

print(LpStatus[status])
print("We need ", value(f), " football trophies.")
print("We need ", value(s), " soccer trophies.")
print("The maximum profit is:", tb1.objective.value())
#HELLO WORLD to PuLP