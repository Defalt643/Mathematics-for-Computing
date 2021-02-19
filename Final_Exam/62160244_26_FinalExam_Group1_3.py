import numpy as np
import math
print('-'*5,'3.1','-'*5)
matrix1 = np.array([[0.15,0.30,0.55]])
matrix2 = np.array([[0,0.2,0.8],[0.4,0,0.6],[0,0.7,0.3]])
num = 100
M = np.dot(matrix1, matrix2)
print('3.1 Next 1 day =',M)
for i in range(2,4):
    M = np.dot(M, matrix2)
    print('3.1 Next',i,'days','=',M)
s1 = (M[0][0]/num)*100
s2 = (M[0][1]/num)*100
print('3.1 Probability of market#2 =',math.ceil(s2*100),'%')
print('-'*5,'3.2','-'*5)
print()
print('-'*5,'3.3','-'*5)
matrix1 = np.array([[0.15,0.30,0.55]])
matrix2 = np.array([[0,0.2,0.8],[0.4,0,0.6],[0,0.7,0.3]])
num = 1
M = np.dot(matrix1, matrix2)
print('Next 1 day =',M)
M1=M
count=1
for i in range(1,50):
    M = np.round(np.dot(M, matrix2),2)
    print('Next',i+1,'day =',M)
    if(np.array_equal(M,M1)):
        break;
    M1=M;
    count=count+1
print("Go to steady state on next",count,"days.")
print('-'*5,'3.4','-'*5)
if any(matrix2[matrix2 == 1]):
    print('This is an absorbing markov chain.')
else:
    print('This is not an absorbing markov chain.')