import numpy as np
print("*"*87)
print("="*87)
print("=>"*20,"ข้อ2.1","<="*20)
matrix2 = np.array([[0.8,0.1,0.1],[0.2,0.7,0.1],[0,0.4,0.6]])
matrix1 = np.array([[0.2,0.3,0.5]])
num = matrix1.sum()
n_e = matrix1.size
print(matrix2)

print('=> Month 1 =',matrix1,'sum =',matrix1.sum())
M = np.dot(matrix1, matrix2)
print('=> Month 2 =',M,'sum =',M.sum())
for i in range(1,4):
    M = np.dot(M, matrix2)
    print('=> Month',i+2,'=',M,'sum =',M.sum())
s1 = (M[0][0]/num)*100
s2 = (M[0][1]/num)*100
s3 = (M[0][2]/num)*100
print('=> S1 =',s1,'%'' and S2 =',s2,'% and S3 =',s3,'%','sum =',M.sum()*100,'%')


print("=>"*20,"ข้อ2.2","<="*20)
if np.count_nonzero(M)==n_e:
    print('=> A is a regular markov chain.')
else:
    print('=> A is not a regular markov chain.')
print()
print("*"*87)
print("="*87)