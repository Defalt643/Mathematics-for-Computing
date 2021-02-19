import numpy as np
from fractions import Fraction
def P(event, space):
    return Fraction(len(event & space), len(space))
dice = np.array([1,2,3,4,5,6])
S = [[x,y] for x in dice for y in dice ]
print("S =",S)
E1 = [[x,y] for x in dice for y in dice if x>3 and  y>3]
print("E1 =",E1)
E2 = [[x,y] for x in dice for y in dice if x+y>6]
print("E2 =",E2)

a = set([tuple(x) for x in E1])
b = set([tuple(x) for x in E2])
E3 = np.array([x for x in a & b])
A = len(E3)/len(S)
P_E1 = len(E1)/len(S)
print("P(B/A) =",P(E3,E1))