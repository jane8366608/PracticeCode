"""
* ZeroJudge d123. 11063 - B2-Sequence
* https://zerojudge.tw/ShowProblem?problemid=d123
* Authored by Yang Yu-Chieh at 2023-05-17 22:01.
* 注意：i可以等於j
"""
from sys import stdin
case = 1
for s in stdin:
    s = int(s)
    A = list(map(int, input().split()))
    B = []
    for i in range(s):
        for j in range(i,s):
            B.append(A[i]+A[j])
    print(f"Case #{case}: It is a B2-Sequence.\n\n" if len(B)==len(list(set(B))) else f"Case #{case}: It is not a B2-Sequence.\n\n")
    case += 1
