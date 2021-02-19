import numpy as np
print("=" * 21, 'ข้อที่2', "=" * 21)
A = np.array([[-6,5,-1],[0,3,4],[-2,1,0]],int)
print(A)
print("="*20,'ข้อที่2.1',"="*20)
print('matrix after remove row #3 col#1')
print(A[np.array([0,1])[:,np.newaxis],np.array([1,2])])
print("="*20,'ข้อที่2.2',"="*20)
print('matrix after remove row #2 col#3')
print(A[np.array([0,2])[:,np.newaxis],np.array([0,1])])
print("="*20,'ข้อที่2.3',"="*20)
def minor(matrix,i,j):
    minor_m = matrix[np.array(list(range(i))+
    list(range(i+1,matrix.shape[0])))[:,np.newaxis],
    np.array(list(range(j))+
    list(range(j+1,matrix.shape[1])))]
    newminor = np.linalg.det(minor_m)
    return newminor

def cofactors(matrix,i,j):
    minor_ij = minor(matrix,i,j)
    newcof = (-1)**(i+j) * minor_ij
    return newcof
r = 2
c = 1
print('M(%d,%d)= ' %(r,c),minor(A,r-1,c-1))
print('C(%d,%d)= ' %(r,c),cofactors(A,r-1,c-1))
print("="*20,'ข้อที่2.4',"="*20)
x = 1
y = 3
print('M(%d,%d)= ' %(r,c),minor(A,x-1,y-1))
print('C(%d,%d)= ' %(r,c),cofactors(A,x-1,y-1))

print('M(%d,%d)= ' %(r,c),minor(A,r-1,c-1))
print('C(%d,%d)= ' %(r,c),cofactors(A,r-1,c-1))
print("="*20,'ข้อที่2.5',"="*20)
def matrix_cofactor(matrix):
    return (np.linalg.inv(matrix)*np.linalg.det(matrix)).transpose()
print('Cof(A) \n', matrix_cofactor(A))
print("="*20,'ข้อที่2.6',"="*20)
def matrix_adj(matrix):
    return np.linalg.inv(matrix)*np.linalg.det(matrix)
print('Adj(A) \n', matrix_adj(A))
print("="*20,'ข้อที่2.7',"="*20)
print('det(A) = ', round(np.linalg.det(A),2))