import numpy as np
m = int(input('number of rows, m = '))
n = int(input('number of columns, n = '))
inputmatrix = [[[] for i in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        print ('entry in row: ',i+1,' column: ',j+1)
        inputmatrix[i][j] = int(input())
matrix =np.array(inputmatrix)
min = matrix.min(axis=0)
O = matrix.max(axis=0)

if (min.max() == O.min()):
    print("min A =", min)
    print("max B =", O)
    print("Maximin of A  =",min.max())
    print("Minimin of B =",O.min())
    print("1.1 Pure Strategy")
else:
    print("min A =",min)
    print("max B =",O)
    print("Maximin of A  =", min.max())
    print("Minimin of B =", O.min())
    print("1.1 Mixed Strategy")
A = matrix.max(axis=1)
B = matrix.min(axis=0)

if (min.max() == O.min()):
    print("Pure Strategy")
    print("Value of the Game = ", min.max())
else:
    print("Mixed Strategy")
    x = matrix[1][0]-matrix[1][1]
    x1 = matrix[0][1]-matrix[1][1]+matrix[1][0]-matrix[0][0]
    P = x/x1
    P1 = 1-P
    print("Probability of A to use","\nStrategy 1 =",round(P,5),",Strategy 2 =",round(P1,5))
    y = matrix[0][1]-matrix[1][1]
    y1 = matrix[1][0]-matrix[1][1]+matrix[0][1]-matrix[0][0]
    Q = y/y1
    Q1 = 1-Q
    print("Probability of B to use","\nStrategy 1 =",round(Q,5),",Strategy 2 =",round(Q1,5))
    ANS = (Q*((matrix[0][0]*P)+(matrix[1][0]*P1)))+(Q1*((matrix[0][1]*P)+(matrix[1][1]*P1)))
A1 = A.max()
B1 = (B.min())
if (A1 > B1):
    print("1.3 A is a Winner and A gain =",A1)
else :
    print("1.3 B is a Winner and A gain =",B1)