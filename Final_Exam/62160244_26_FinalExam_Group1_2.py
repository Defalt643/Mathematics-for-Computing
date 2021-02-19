import numpy as np
from fractions import Fraction
faces = np.array(["H","T"])
num = np.array([1,2,3,4,5,6])
S = [[o,x,y,z] for o in num for x in num for y in faces for z in faces]
print("2.1 S =",S)
print("2.1 n(S) =",len(S))
print('-'*60)
E1 =[[o,x,y,z] for o in num for x in num for y in faces for z in faces if (o+x)%2==1]
print("2.2 E2_2 =",E1)
print("2.2 n(E2_2) =",len(E1))
print("2.2 P(E2_2 =",len(E1)/len(S))
print('-'*60)
E2=[[o,x,y,z] for o in num for x in num for y in faces for z in faces if y=='H' and z=='H']
print("2.3 E2_3",E2)
print("2.3 n(E2_3) =",len(E2))
print("2.3 P(E2_3) =",len(E2)/len(S))
print('-'*60)
E3=[[o,x,y,z] for o in num for x in num for y in faces for z in faces if y!=z and x==o]
print("2.4 E2_4",E3)
print("2.4 n(E2_4) =",len(E3))
print("2.4 P(E2_4) =",len(E3)/len(S))
print('-'*60)