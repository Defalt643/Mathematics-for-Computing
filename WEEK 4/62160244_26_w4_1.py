import numpy as np
matrixA = np.array([[4,2,1],[2,0,-2],[1,-3,2]])
matrixB = np.array([[10,15,6]])
detA = np.linalg.det(matrixA)
print('DetA = ',detA)
def Cramer(matrixA,matrixB,i,detA):
    MAcopy = matrixA[:,i].copy()
    matrixA[:,i] = matrixB
    print(matrixA)
    x = np.linalg.det(matrixA)/detA
    matrixA[:,i] = MAcopy.copy()
    return x
if detA==0:
    sys.exit("No solutions, the coefficient matrix(A)have a zero determinant")
else:
    for i in range(matrixA.shape[0]):
        Ans = Cramer(matrixA,matrixB,i,detA)
        print('X',i+1,'= ',Ans)
