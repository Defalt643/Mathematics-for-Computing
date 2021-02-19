print("="*20,'ข้อที่1.1',"="*20)
import numpy as np
matrix1 = np.array([[0,-2],[3,0]])
matrix2 = np.array([[1,5],[5,1]])
matrix3 = np.array([[0,2],[-3,0]])
ans1 = 2*(matrix1+matrix2)
print('1.1) 2(A + B)\n',ans1)

print("="*20,'ข้อที่1.2',"="*20)
ans2 = 2*matrix1+(matrix3-matrix2)
print('1.2) 2A + (C - B)\n',ans2)

print("="*20,'ข้อที่1.3',"="*20)
matrix1_t = matrix1.transpose()
ans3 = matrix1_t + (2*matrix2)
print(ans3)

print("="*20,'ข้อที่1.4',"="*20)
BA = np.dot(matrix1,matrix2)
AB = np.dot(matrix2,matrix1)
if np.array_equal(BA,AB):
    print("Yes")
else:
    print("No")

print("="*20,'ข้อที่1.5',"="*20)
if np.array_equal(matrix1,-matrix3):
    print("Yes")
else:
    print("No")

print("="*20,'ข้อที่1.6',"="*20)
matrix2_t = matrix2.transpose()
if np.array_equal(matrix2,matrix2_t):
    print("Yes")
else:
    print("No")

print("="*20,'ข้อที่1.7',"="*20)
matrix3_t = matrix3.transpose()
if np.array_equal(matrix3_t,-matrix3):
    print("Yes")
else:
    print("No")

print("="*20,'ข้อที่1.8',"="*20)
AC = np.dot(matrix1,matrix3)
AC_t = AC.transpose()
At_Ct = np.dot(matrix1_t,matrix3_t)
if np.array_equal(AC_t,At_Ct):
    print("Yes")
else:
    print("No")
print("="*20,'ข้อที่2.1',"="*20)
A = np.array([[-2,0,0],[0,1,0],[0,0,3]])
B = np.array([[4,0,0],[0,4,0],[0,0,4]])
C = np.array([[3,0,0],[6,7,0],[9,10,11]])
AB = np.dot(A,B)
A_t = A.transpose()
B_t = B.transpose()
C_t = C.transpose()
ans4 = 2*(np.dot(B,A))
print(ans4)
print("="*20,'ข้อที่2.2',"="*20)
X = 3*(A+B)
Y = (3*A)+(3*B)
if np.array_equal(X,Y):
    print("Yes")
else:
    print("No")

print("=" * 20, 'ข้อที่2.3', "=" * 20)
AB_t = AB.transpose()
Bt_At = np.dot(B_t,A_t)
if np.array_equal(AB_t,Bt_At):
    print("Yes")
else:
    print("No")

print("=" * 20, 'ข้อที่2.4', "=" * 20)
BC = B+C
B_C_t = B_t+C_t
BC_t = BC.transpose
if np.array_equal(BC_t,B_C_t):
    print("Yes")
else:
    print("No")
print("=" * 20, 'ข้อที่2.5', "=" * 20)
print("A^4\n",A**4)
print("B^4\n",B**3)
print("C^4\n",C**2)