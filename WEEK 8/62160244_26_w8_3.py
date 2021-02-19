import numpy as np
matrix=np.array([[-2,-5,16],[-4,10,-8]])
print(matrix)
A = matrix.min(axis=1)
print("min A =",A)
B = matrix.max(axis=0)
print("max B =",B)
print("Maximin =",A.max(),"AND strategyA =",np.argmax(A)+1)
print("Minimax =",B.min(),"AND strategyB =",np.argmin(B)+1)
if (A.max() == B.min()):
    print("Value of the Game = ",A.max())
    print("Maximin = Minimax")
    print("This game is Pure Strategy")
else:
    print("Maximin != Minimax")
    print("This game is Mixed Strategy")
if (A.max() == B.min()):
    A1 = A.max()
    B1 = (B.min()*(-1))
    if (A1 > B1):
        print("A is a Winner")
        print("A profit = ",A1,"Million Baht")
        print("B lost = ", -B1,"Million Baht")
    else :
        print("B is a Winner")
        print("B profit = ",B1,"Million Baht")
        print("A lost = ", -A1,"Million Baht")
print(A.max())
print(B.min())
