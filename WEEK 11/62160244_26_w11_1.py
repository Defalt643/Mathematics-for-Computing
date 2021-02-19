print("=>"*20,"ข้อ1.1","<="*20)
import numpy as np
matrix1 = np.array([[600,400]])
matrix2 = np.array([[0.7,0.3],[0.2,0.8]])
num = 1000
M = np.dot(matrix1, matrix2)
print('End of year 1 =',M)
for i in range(1,3):
    M = np.dot(M, matrix2)
    print('End of years',i+1,'=',M)
s1 = (M[0][0]/num)*100
s2 = (M[0][1]/num)*100
print('S1 =',s1,'% and S2 =',s2,'%')

print("=>"*20,"ข้อ1.2","<="*20)
print("=>","SKIP "*16,"<=")
print("=>","SKIP "*16,"<=")
print("=>","SKIP "*16,"<=")

print("=>"*20,"ข้อ1.3","<="*20)
M = np.dot(matrix1, matrix2)
print('End of years 1 =',M)
for i in range(1,2):
    M = np.dot(M, matrix2)
    print('End of years',i+1,'=',M)
s1 = (M[0][0]/num)*100
s2 = (M[0][1]/num)*100
print('S1 =',s1,'% and S2 =',s2,'%')

print("=>"*20,"ข้อ1.4","<="*20)
matrix1 = np.array([[600,400]])
matrix2 = np.array([[0.7,0.3],[0.2,0.8]])
num = 1000
M = np.dot(matrix1, matrix2)
print('End of month 1 =',M)
M1=M
count=1
for i in range(1,50):
    M = np.round(np.dot(M, matrix2),2)
    print('End of month',i+1,'=',M)
    if(np.array_equal(M,M1)):
        break;
    M1=M;
    count=count+1
print("Go to steady state at",count,"month")
s1 = (M[0][0]/num)*100
s2 = (M[0][1]/num)*100
print("Single women is",s2,"percent")

print("=>"*20,"ข้อ1.5","<="*20)
if any(matrix2[matrix2 == 1]):
    print('A is a Absorbing Markov Chain.')
else:
    print('A is not a Absorbing Markov Chain.')