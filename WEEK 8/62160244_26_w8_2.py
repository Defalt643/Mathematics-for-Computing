import numpy as np
m = int(input('number of rows, m = '))
n = int(input('number of columns, n = '))
inputmatrix = [[[] for i in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        print ('entry in row: ',i+1,' column: ',j+1)
        inputmatrix[i][j] = int(input())
matrix = np.array(inputmatrix)
print(matrix)
A = matrix.min(axis=1)
print("min A =",A)
B = matrix.max(axis=0)
print("max B =",B)
print("Maximin =",A.max(),"AND strategyA =",np.argmax(A)+1)
print("Minimax = ",B.min(),"AND strategyB =",np.argmin(B)+1)
if (A.max() == B.min()):
    print("Value of the Game = ",A.max())
    print("Pure Strategy")
    A1 = A.max()
    B1 = (B.min()*(-1))
    if (A1 > B1):
        print("A is a Winner")
        print("A profit = ", A1)
    else :
        print("B is a Winner")
        print("B profit = ", B1)
else:
    print("Mixed Strategy")
    A1 = A.max()
    B1 = (B.min() * (-1))
    if (A1 > B1):
        print("A is a Winner")
        print("A profit = ", A1)
        print("B lost = ",-B1)
    else :
        print("B is a Winner")
        print("B profit = ", B1)
        print("A lost = ",-A1)