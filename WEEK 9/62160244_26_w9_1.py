import numpy as np
dice = np.array([1,2,3,4,5,6])
S = [[x,y,z] for x in dice for y in dice for z in dice]
print("n(S) =",len(S))
print("S =",S)
s1 = [[x,y] for x in dice for y in dice]
E1 = [[x,y] for x in dice for y in dice  if (x+y>6) and x==y ]
print("E1 =",E1)
print(len(E1))
print(len(s1))
E2 = [[x,y,z] for x in dice for y in dice for z in dice if x == y == z]
print("E2 =",E2)
print("A"+1+2+"B")