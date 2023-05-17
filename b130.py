"""
* ZeroJudge b130. NOIP2006 1.明明的随机数
* https://zerojudge.tw/ShowProblem?problemid=b130
* Authored by Yang Yu-Chieh at 2023-05-17 22:23.
* 
"""
from sys import stdin
for N in stdin:
    A = list(map(int,input().split()))
    A = list(set(A))
    A.sort()
    print(len(A))
    for x in A:
        print(x, end=" ")
