from fractions import Fraction
import itertools
from math import factorial
import numpy as np

def P(event, space):
    return Fraction(len(event & space), len(space))

def cross (A,B,C):
    return {a+b+c for a in A for b in B for c in C}

S = cross('HT','HT','HT')
print(S)
print(len(S))

E1 = {s for s in S if s[0] != 'H' and s[1] != 'H' and s[2] != 'H'}
print(E1)
A = P(E1,S)
print('P(A) = ',A)

E2 = {s for s in S if s[0] == 'H' and s[1] != 'H' and s[2] != 'H' or s[0] != 'H' and s[1] == 'H' and s[2] != 'H' or s[0] != 'H' and s[1] != 'H' and s[2] == 'H'}
print('E2',E2)
B = P(E2,S)
print('P(B) = ',B)

E3 = {s for s in S if s[1] == 'T' and s[2] == 'T'}
print('E3',E3)
C = P(E3,S)
print('P(C) = ',C)

a = set([tuple(x) for x in E1])
b = set([tuple(x) for x in E2])
C = np.array([x for x in a & b])
print('A intersect B) = ',(C))
AB = len(C)/len(S)
print('P(A intersect ) = ',AB)

a = set([tuple(x) for x in E2])
b = set([tuple(x) for x in E3])
C = np.array([x for x in a & b])
print('B intersect C = ',(C))
BC = len(C)/len(S)
print('P(B intersect C) = ',BC)

a = set([tuple(x) for x in E1])
b = set([tuple(x) for x in E3])
C = np.array([x for x in a & b])
print('A intersect C = ',(C))
AC = len(C)/len(S)
print('P(A intersect C) = ',AC)


if (AB == BC == AC):
    print("YES")
else:
    print("NO")