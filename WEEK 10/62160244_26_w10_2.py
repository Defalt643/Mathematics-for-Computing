# from fractions import Fraction
#
# def P(event, space):
#     return Fraction(len(event & space), len(space))
#
# def cross(A, B):
#     return {a + b for a in A for b in B}
#
# S = cross('X', 'A234567890JQK') | cross('Y', 'A234567890JQK')| cross('Z', 'A234567890JQK')|cross('O', 'A234567890JQK')
# print(S)
# print("n(S) =",len(S))
#
# import itertools
#
# def combos(items, n):
#     return {' '.join(combo)
#         for combo in itertools.combinations(items, n)}
#
# U3 = combos(S, 3)
#
#
# from math import factorial
#
# def choose(n, r):
#     return factorial(n) // (factorial(n - r) * factorial(r))
#
#
#
# E1 = {s for s in U3 if s.count('O') == 2 and s.count('Z') and s.count('Z')}
#
# print("E1 =",E1)
# print("P(E1) =",P(E1,U3))
# E2 = {s for s in U3 if s.count('X') == 'K' or s.count('Y') == 'K' or s.count('Z') == 'K' or s.count('O') == 'K'}
# print("E2 =",E2)
# print("P(E2)= ",P(E2, U3))
# E3 = {s for s in U3 if s.count('Y') and s.count('X') and s.count('Z')}
# print("E3 =",E3)
# print("P(E3) =",len(E3))

import itertools
def combos(items, n):
    return {' '.join(combo)
        for combo in itertools.combinations(items, n)}
def cross(A, B):
    return {a + b for a in A for b in B}
from math import factorial
def choose(n, r):
    return factorial(n) // (factorial(n - r) * factorial(r))
S = cross('X','A234567890JQK') | cross('Y','A234567890JQK') | cross('Z','A234567890JQK') | cross('W','A234567890JQK')
print(S)
n_S = choose(52,3)
print("2.1  หาไพ่ข้าวหลามตัด1ใบ และอีก2ใบเป็นดอกจิก")
A =choose(13,1)
B =choose(13,2)
print(" Ans = ",(A*B)/n_S)
print(".................................")
print("2.2 ความน่าจะเป็นที่จะได้ไพ่ K 3ใบ")
C = choose(4,3)
print(" Ans = ",C/n_S)
print(".................................")
print("2.3 ความน่าจะเป็นที่จะได้ไพ่สีแดง1ใบ สีดำ3ใบ")
D = choose(26,1)
E = choose(26,2)
print(" Ans = ",D*E/n_S)