import numpy as np
print("="*21,'ข้อที่1',"="*21)
A = np.array([[2,-4],[10,-3]],int)
B = np.array([[-5,1],[9,-2]],int)
print(A)
print("="*20,'ข้อที่1.1',"="*20)
print('det(A) = ', round(np.linalg.det(A),2))
print("="*20,'ข้อที่1.2',"="*20)
print('det(B) = ', round(np.linalg.det(B)),)
print("="*20,'ข้อที่1.3',"="*20)
A_in = np.linalg.inv(A)
B_in = np.linalg.inv(B)
print('inverse(A) \n', A_in)
print('inverse(B) \n', B_in)
print("="*20,'ข้อที่1.4',"="*20)
det_B =round(np.linalg.det(B),2)
det_B_in=round(np.linalg.det(B_in),2)
if np.array_equal(det_B,det_B_in):
    print("Yes")
else:
    print("No")
print("="*20,'ข้อที่1.5',"="*20)
det_A = round(np.linalg.det(A),2)
det_A_in = round(np.linalg.det(A_in),2)
det_A_T = round(1/np.linalg.det(A.transpose()),2)
if np.array_equal(det_A_in,(det_A_T)):
    print("Yes")
else:
    print("No")
