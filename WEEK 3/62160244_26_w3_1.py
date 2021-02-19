import numpy as np
import sys
print("="*40,"ข้อที่1.1","="*40)
A = np.array([[2,-4,1],[3,1,-2],[1,0,5]])
print(A)
print("Det A = ", round(np.linalg.det(A)))
print("="*40,"ข้อที่1.2","="*40)
def inversematrix(matrix):
    matrixI = np.identity(matrix.shape[0])
    matrixT = np.concatenate((matrix, matrixI.T), axis=1)
    print('matrix = ',matrix)
    print(' ')
    print('matrix[A:I] = ',matrixT)
    print(' ')
    y = 0
    z = 0
    c = 0
    for j in range(matrix.shape[0]):
        x = matrixT[y][z]
        for i in range(len(matrixT[0])):
            matrixT[j][i] = matrixT[j][i]/x
        print('Row',j+1,' / ',x)
        print(matrixT)
        for j in range(matrixT.shape[0]):
            if(matrixT[j][c] != 0 and matrixT[j][c] == 1 and j != c):
                d = matrixT[j][c]
                print('Row',j+1,' - Row',c+1)
                for i in range(len(matrixT[0])):
                    matrixT[j][i] = matrixT[j][i] - matrixT[c][i]
                print(matrixT)
            elif (matrixT[j][c] != 0 and ((matrixT[j][c] > 1) or (matrixT[j][c] < 1))):
                d = matrixT[j][c]
                print('Row',j+1,' - ',d,'*Row',c+1)
                for i in range(len(matrixT[0])):
                    matrixT[j][i] = matrixT[j][i] - (d*matrixT[c][i])
        print(matrixT)
        print(' ')
        c += 1
        y += 1
        z += 1
        print(matrixT)
        Newmatrix = np.delete(matrixT,np.s_[:matrix.shape[0]],1)
        print(' ')
        print('matrix A = ')
        print(np.array(matrix))
        print('Inverse matrix A = ')
        print(Newmatrix)
        print(' ')
        print('Test (A x Inverse A) = I ?')
        print(np.round(np.dot(matrix,Newmatrix)))

matrix = np.array([[2,-4,1],[3,1,-2],[1,0,5]])
print(matrix)
if matrix[0][0]==0:
    for i in range(1,matrix.shape[0]):
        if matrix[i][0]!=0:
            matrix[[0, i]] = matrix[[i, 0]]
            break
    else:
        sys.exit("THE MATRIX IS NOT INVERTIBLE")

inversematrix(matrix)
print("="*40,"ข้อที่1.3","="*40)
print("Rank A = ",np.linalg.matrix_rank(A))
print("="*40,"ข้อที่1.4","="*40)
A_I = np.linalg.inv(A)
AxA_I=np.round(np.dot(A,A_I),0)
print("Matrix A\n",A,"\nInverse matrix A \n",A_I)
print("A x A^-1 \n",AxA_I)
I = np.identity(3)
if np.array_equal(AxA_I,I):
    print("Yes")
else:
    print("No")
