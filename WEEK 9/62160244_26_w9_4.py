# S = list(range(1,11))
# print("S =",S)
# E1 = [[x,y] for x in S for y in S if (x+y)%2==0 and x!=y]
# print("n(S) =",len(E1))
# print("E1 =",E1)
# E2 = [[x,y] for x in S for y in S if x+y<12 and x!=y]
# print("E2 =",E2)
# E3 = [[x,y] for x in S for y in S if (x+y)%2==0 and x+y<12 and x!=y and x<5 ]
# print("E3 =",E3)
# print("n(E1 intersection E2) =",len(E3))
# print("P(E1 intersection E2) =",(10/45))
import numpy as np
import math
S = np.array([1,2,3,4,5,6,7,8,9,10])
def combination(n,r):
    C = math.factorial(n)/(math.factorial(n-r)*
        math.factorial(r))
    return C
E1 = [[x,y] for x in S for y in S if (x+y)%2 ==0]
E2 = [[x,y] for x in S for y in S if (x+y) < 12]

a = set([tuple(x) for x in E1])
b = set([tuple(x) for x in E2])
E3 = np.array([x for x in a & b])
print("E1 interest E2 =",E3)
E3 = np.intersect1d(E1, E2)
print("n(E) =",len(E3))
n_S = combination(10,2)
print("n(S) =",n_S)

print("P(E)=",len(E3)/n_S)
