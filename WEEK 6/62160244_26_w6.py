import matplotlib.pyplot as plt
import numpy as np
from matplotlib.legend_handler import HandlerLine2D
x=0
y=0
X1 = (250-5*(x))/2
X2 = (250-2*(y))/5
a = [x,X2]
b = [X1,y]

X11 = (150-1*(x))/2
X22 = (150-2*(y))/1
a1 = [x,X22]
b1 = [X11,y]

p1 = [0,125]
p2 = [40,40]

Car_Pa = np.array([[5, 2],[ 1, 2]])#blue up
AnsCar_Pa = np.array([250,150])

Car_Ch = np.array([[ 5, 2],[ 1, 0]])#blue down
AnsCar_Ch = np.array([250,40])

Ch_Y = np.array([[ 1, 0],[ 0, 1]])
AnsCh_Y = np.array([40,0])

Pa_X = np.array([[ 1, 2],[1,0]])
AnsPa_X = np.array([150,0])

def solve(A,B):
    Anssolve = np.array(np.linalg.solve(A, B))
    z = 20*Anssolve[0] + 30*Anssolve[1]
    return [Anssolve,z]

intersection1 = solve(Ch_Y,AnsCh_Y)
print('Point 2 = ',intersection1[0], 'Z = ',intersection1[1])
plt.plot(intersection1[0][0],intersection1[0][1],'ro')
k = np.array([intersection1[1]])
Newintersection1 = np.concatenate((intersection1[0], k), axis=0)

intersection2 = solve(Car_Ch,AnsCar_Ch)
print('Point 3 = ',intersection2[0], 'Z = ',intersection2[1])
plt.plot(intersection2[0][0],intersection2[0][1],'ro')
k1 = np.array([intersection2[1]])
Newintersection2 = np.concatenate((intersection2[0], k1), axis=0)

intersection3 = solve(Car_Pa,AnsCar_Pa)
print('Point 4 = ',intersection3[0], 'Z = ',intersection3[1])
plt.plot(intersection3[0][0],intersection3[0][1],'ro')
k2 = np.array([intersection3[1]])
Newintersection3 = np.concatenate((intersection3[0], k2), axis=0)

intersection4 = solve(Pa_X,AnsPa_X)

print('Point 5 = ',intersection4[0], 'Z = ',intersection4[1])
plt.plot(intersection4[0][0],intersection4[0][1],'ro')
k3 = np.array([intersection4[1]])
Newintersection4 = np.concatenate((intersection4[0], k3), axis=0)

N1 = np.array([Newintersection1])
N2 = np.array([Newintersection2])
N3 = np.array([Newintersection3])
N4 = np.array([Newintersection4])
New = np.concatenate((N1, N2), axis=0)
New = np.concatenate((New, N3), axis=0)
New = np.concatenate((New, N4), axis=0)
#print(New)

Newmatrix = np.delete(New,np.s_[:2],1)

max = np.amax(Newmatrix)
print('Mni = ',min)

p = np.nonzero(Newmatrix.min() == Newmatrix)
n = p[0]
n1 = New[n]
print('T = ',n1[0][0],'C = ',n1[0][1])

AnsC = (max-20*(x))/30
AnsT = (max-30*(y))/20
Ansa = [x,AnsT]
Ansb = [AnsC,y]

line1,=plt.plot(a,b,label='Constrint 1')
plt.plot(a1,b1,label='Constrint 2')
plt.plot(p2,p1,label='Constrint 3')
plt.plot(Ansa,Ansb,label='IsoCost Line : at MIN point')
plt.legend(handler_map={line1: HandlerLine2D(numpoints=4)})

shade1 =[intersection1[0][0],intersection2[0][0],intersection3[0][0],intersection4[0][0]]
shade2 =[intersection1[0][1],intersection2[0][1],intersection3[0][1],intersection4[0][1]]

plt.grid('on')
plt.fill_between(shade1,shade2, color='blue', alpha='0.5')
plt.fill(shade1,shade2)
plt.ylabel('x2')
plt.xlabel('x1')
plt.show()