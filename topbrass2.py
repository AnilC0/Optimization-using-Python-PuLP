"""
@AnilC
Top Brass Problem
"""
sports = ("football"), ("soccer")
wood = {"football":4, "soccer":2}
plaques = {"football":1, "soccer":1}
profit = {"football":12, "soccer":9}
nwood, nplaques = 4800, 1750
nfootball, nsoccer = 1000, 1500

from pulp import *

trophies =LpVariable.dict("trophies",[(s) for s in sports],0) 
tplaques = LpAffineExpression(sum(trophies[i]*plaques[i] for i in sports),name="tplaques")
twood = LpAffineExpression(sum(trophies[i]*wood[i] for i in sports),name="twood")
tprofit = LpAffineExpression(sum(trophies[i]*profit[i] for i in sports),name="tprofit")

tb2 = LpProblem("tb2",LpMaximize)
tb2 += trophies["soccer"] <= nsoccer
tb2 += trophies["football"] <= nfootball
tb2 += tplaques <= nplaques
tb2 += twood <= nwood
tb2 += tprofit
status = tb2.solve()

# print part
print(LpStatus[status])
print("We need to build ", value(trophies["football"]), " football trophies.")
print("We need to build ", value(trophies["soccer"]), " soccer trophies.")
print("The maximum profit possible is:" , value(tprofit))
