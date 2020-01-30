"""
@AnilC
Sailco Problem
"""
demand = [40, 60, 70, 25]	# monthly demand for boats

from pulp import *

rLabor = LpVariable.dict("rLabor", range(0,4), 0, 40,"Integer") 
oLabor = LpVariable.dict("oLabor", range(0,4), 0,cat="Integer")
holded = LpVariable.dict("holded", range(0,5), 0,cat="Integer")

sailco = LpProblem("sailco", LpMinimize)
sailco += holded[0] == 10
for i in range(0,4):
	sailco += holded[i] + rLabor[i] + oLabor[i] == demand[i] + holded[i+1]
sailco += 400*lpSum(rLabor) + 450*lpSum(oLabor) + 20*lpSum(holded)

#print(sailco)  #good for debugging
status = sailco.solve()

print("Quarterly boat demand:\t",demand[0], demand[1], demand[2], demand[3])
print("Regular labor need:\t"  ,value(rLabor[0]), value(rLabor[1]), value(rLabor[2]), value(rLabor[3]))
print("Overtime labor need:\t" ,value(oLabor[0]), value(oLabor[1]), value(oLabor[2]), value(oLabor[3]))
print("Boats holded in hand:\t",value(holded[0]), value(holded[1]), value(holded[2]), value(holded[3]))
print(sailco.objective.value(),"$")

