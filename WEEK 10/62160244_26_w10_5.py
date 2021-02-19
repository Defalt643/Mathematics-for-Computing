import numpy as np
from fractions import  Fraction
import math

tow = np.array([1,2,3,4,5,6])


S = [[x,y] for x in tow for y in tow]
print(S)
print('n(S) = ',len(S))

A = [[x,y] for x in tow for y in tow if (x+y == 9)]
print('n(A) = ',len(A))

B = [[x,y] for x in tow for y in tow if (x <= y)]
print('n(B) = ',len(B))

a = set([tuple(x) for x in A])
b = set([tuple(x) for x in B])
C = np.array([x for x in a & b])
print('A intersect B = ',len(C))
PA = len(A)/len(S)
PB = len(B)/len(S)
PAB = len(C)/len(S)
print('P(A) = ',PA)
print('P(B) = ',PB)

print('P(A/B) = ',PAB / PB)
print('P(B/A) = ',PAB / PA)