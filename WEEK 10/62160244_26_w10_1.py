import  numpy as np
dice = np.array([1,2,3,4,5,6])
baht = np.array(["H", "T"])
S = [[x, y, z] for x in dice for y in baht for z in baht ]
print("S =", S)
E1 = [[x, y, z] for x in dice for y in baht for z in baht if x > 5]
print("E1 =", E1)
E2 = [[x, y, z] for x in dice for y in baht for z in baht if y == z]
print("E2 =", E2)
a = set([tuple(x) for x in E1])
b = set([tuple(x) for x in E2])
E3 = np.array([x for x in a & b])
P_A = len(E1)/len(S)
P_B = len(E2)/len(S)
A = P_A*P_B
B = len(E3)/len(S)
if(B == A):
    print("YES")
else:
    print("NO")