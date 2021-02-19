import numpy as np
matrixA = np.array([[2,1,2,1],[2,2,5,1],[0,-2,8,2],[3,1,-1,4]],float)
matrixB = np.array([[2,8,10,24]],float)
def Gaussian(matrixA,matrixB):
    summatrix = np.concatenate((matrixA, matrixB.T), axis=1)
    print(summatrix)
    y = 0
    z = 0
    c = 0
    for j in range(matrixA.shape[0]):
        x = summatrix[y][z]
        for i in range(len(summatrix[0])):
            summatrix[j][i] = summatrix[j][i]/x
        #print('row',j+1,' / ',x)
        #print(summatrix)
        for j in range(summatrix.shape[0]):
            if(summatrix[j][c] != 0 and summatrix[j][c] == 1 and j != c):
                d = summatrix[j][c]
                #print('Row',j+1,' - Row',c+1)
                for i in range(len(summatrix[0])):
                    summatrix[j][i] = summatrix[j][i] - summatrix[c][i]
                    #print(summatrix)
            elif(summatrix[j][c] != 0 and ((summatrix[j][c]>1) or (summatrix[j][c]<1 ))):
                d = summatrix[j][c]
                #print('Row',j+1,' - ',d,'*Row',c+1)
                for i in range(len(summatrix[0])):
                    summatrix[j][i] = summatrix[j][i] - (d*summatrix[c][i])
            #print(summatrix)
        print(' ')
        c += 1
        y += 1
        z += 1
    np.set_printoptions(suppress=True)
    print(summatrix)
    Nmatrix = np.delete(summatrix,np.s_[:matrixA.shape[0]],1)
    return Nmatrix

Ans = Gaussian(matrixA,matrixB)
for i in range(Ans.shape[0]):
    print('x',i+1,' = ',Ans[i])