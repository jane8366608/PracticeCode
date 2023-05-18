"""
* ZeroJudge c813. 11332 - Summing Digits
* https://zerojudge.tw/ShowProblem?problemid=c813
* Authored by Yang Yu-Chieh at 2023-05-18 15:44.
* 
"""
from sys import stdin
def f(N):
    A = [int(x) for x in str(N)]
    return sum(A)

def g(N):
    while N>9:
        N = f(N)
    return N
        

for read in stdin:
    N = int(read)
    if N==0: 
        break
    print(g(N))
