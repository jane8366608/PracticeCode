"""
* ZeroJudge d673. 11608 - No Problem
* https://zerojudge.tw/ShowProblem?problemid=d673
* Authored by Yang Yu-Chieh at 2023-05-17 23:30.
* 
"""
from sys import stdin
case = 1
for S in stdin:
    S = int(S)
    if S<0:
        break
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    print(f"Case {case}:")
    case += 1
    for i in range(12):
        if S>=B[i]:
            print("No problem! :D")
            S = S+A[i]-B[i]
        else:
            S = S+A[i]
            print("No problem. :(")
