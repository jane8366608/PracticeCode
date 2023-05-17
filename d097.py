"""
* ZeroJudge d097. 10038 - Jolly Jumpers
* https://zerojudge.tw/ShowProblem?problemid=d097
* Authored by Yang Yu-Chieh at 2023-05-17 21:26.
* 
"""
from sys import stdin
for s in stdin:
    A = list(map(int, s.split()))
    mat = [x for x in range(1,A[0])]
    B = []
    for i in range(1,A[0]):
        tmp=abs(A[i+1]-A[i])
        if tmp>=1 and tmp<=A[0]-1:
            B.append(tmp)
    B.sort()
    print("Not jolly" if B!=mat else "Jolly")
    
