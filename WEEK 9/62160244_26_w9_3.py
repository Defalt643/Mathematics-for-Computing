import numpy as np

print("*"*50,"ข้อ3.1","*"*50)
S = list(range(1,47))
print("n(S) =",len(S))
print("S =",S)
E1 = [x for x in S if x%3 == 0]
print("E1 =",E1)
print("*"*50,"ข้อ3.2","*"*50)
E2 = [x for x in S if x%5 == 0]
print("E2 =",E2)
print("*"*50,"ข้อ3.3","*"*50)
E3 = [x for x in S if (x%5)== 0 and (x%3) == 0]
print("E3 =",E3)
print("*"*50,"ข้อ3.4","*"*50)
E4 = [x for x in S if (x%5)== 0 or (x%3) == 0]
print("E4 =",E4)