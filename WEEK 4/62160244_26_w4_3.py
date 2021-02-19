import numpy as np
matrixA = np.array([[8,1,0],[3,-2,2],[1,2,3]],float)
matrixB = np.array([[0,0,0]],float)

def GaussianReduced(matrixA,matrixB):
    summatrix = np.concatenate((matrixA, matrixB.T), axis=1)
    print(summatrix)
    y = 0
    z = 0
    c = 0
    for j in range(summatrix.shape[0]):
        x = summatrix[y][z]
        if(x != 0):
            for i in range(len(summatrix[0])):
                summatrix[j][i] = summatrix[j][i]/x
            #print('Row',j+1,' / ',x)
            #print(summatrix)
            for j in range(summatrix.shape[0]):
                if(summatrix[j][c] != 0 and summatrix[j][c] ==1 and j != c):
                    d = summatrix[j][c]

                #print('Row',j+1,' - Row',c+1)
                for i in range(len(summatrix[0])):
                    summatrix[j][i] = summatrix[j][i]-summatrix[c][i]
                    #print(summatrix)
        elif (summatrix[j][c] != 0 and ((summatrix[j][c]>1)or (summatrix[j][c]<1 ))):
            d = summatrix[j][c]
            #print('Row',j+1,' - ',d,'*Row',c+1)
            for i in range(len(summatrix[0])):
                summatrix[j][i] = summatrix[j][i]-(d*summatrix[c][i])
            #print(summatrix)
            c += 1
            y += 1
            z += 1
        else:
            break
    return [summatrix,j]

detA = np.linalg.det(matrixA)
print('detA =',round(detA))

if np.array_equal(matrixB, np.zeros((1,matrixB.shape[1]))):
    if round(detA)!=0:
        for i in range(matrixA.shape[0]):
            print('x', i + 1, ' = 0')

    else:
        Ans = GaussianReduced(matrixA,matrixB)
        matrix = Ans[0]
        num = Ans[1]
        print(matrix)
        matrix1 = np.delete(matrix,np.s_[:matrix.shape[0]],1)
        matrix2 = np.delete(matrix,np.s_[:num],1)
        matrix2 = np.delete(matrix2,np.s_[1:],1)

        for i in range(matrix2.shape[0]):
            if(matrix2[i] != 0):
                print('x',i+1,' = ',matrix2[i],'x',num+1)
            else:
                print('x',i+1,' = Free')
if detA ==0:
    print("มีคำตอบหลายชุด")
else:
    print("มีคำตอบเดียวตือ X = 0")