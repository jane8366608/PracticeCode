"""
* ZeroJudge c085. 00350 - Pseudo-Random Numbers
* https://zerojudge.tw/ShowProblem?problemid=c085
* Authored by Yang Yu-Chieh at 2023-05-17 20:19.
* 
"""
from sys import stdin
case = 1
for s in stdin:
    Z, I, M, L = map(int, s.split())
    firstL = L
    if sum([Z,I,L,M])==0:
        break
    mat = []
    cnt = 0
    while L not in mat:
        mat.append(L)
        L = (Z*L+I)%M
        cnt += 1
    
    print(f"Case {case}: {cnt}" if firstL==L else f"Case {case}: {cnt-1}")
    case += 1        
    
