import numpy as np
faces = np.array(["H","T"])
num = np.array([1,2,3,4,5,6])
S = [[o,x,y,z] for o in num for x in num for y in faces for z in faces]
print("n(S) =",len(S))
print("S =",S)
E1 = [[x,y,z] for x in faces for y in faces
for z in faces if (x == "H" and y =="H" and z != "H")or (x == "H" and y == "H" and z =="H")or ( x != "H" and y == "H" and z =="H" )or( x != "H" and y == "H" and z !="H" )]
print("E1 =",E1)
E2 = [[x,y,z] for x in faces for y in faces
for z in faces if (x == "T") ]
print("E2 =",E2)
a = set([tuple(x) for x in E1])
b = set([tuple(x) for x in E2])
E3 = np.array([x for x in a & b])
print("E1 intersection E2 =",E3)
print("n(E1 intersection E2) =",len(E3))
print("P(E1 intersection E2) =",len(E3)/len(S))
