import numpy as np
matrixA = np.array([[5,2,4],[-2,1,1],[1,-2,0]])
matrixB = np.array([[15,12,24]])
def minor(matrix,i,j):
    minor_m = matrix[np.array(list(range(i))+
    list(range(i+1,matrix.shape[0])))[:,np.newaxis],np.array(list(range(j))+list(range(j+1,matrix.shape[1])))]
    newminor = np.linalg.det(minor_m)
    return newminor

def cofactors_m(matrix):
    newcof = np.zeros(matrix.shape)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            minor_ij = minor(matrix,i,j)
            newcof[i,j] = (-1)**(i+j) * minor_ij
    return newcof

def inverse(matrixA,matrixB,matrixCT):
    det = np.linalg.det(matrixA)
    inverseAB = 1/ det *(np.dot(matrixCT,matrixB.transpose()))
    return inverseAB
print("="*40,"ข้อที่2.1","="*40)
print('Cof(A)\n',np.round(cofactors_m(matrixA)))
print("="*40,"ข้อที่2.2","="*40)
print('Adj(A)\n',np.round(cofactors_m(matrixA).transpose()))
print("="*40,"ข้อที่2.3","="*40)
ansinverse = inverse(matrixA,matrixB,cofactors_m(matrixA).transpose())
print(ansinverse)
for i in range(ansinverse.shape[0]):
    print('x',i+1,' = ',ansinverse[i])