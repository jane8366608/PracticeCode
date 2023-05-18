"""
* ZeroJudge c002. 10696 - f91
* https://zerojudge.tw/ShowProblem?problemid=c002
* Authored by Yang Yu-Chieh at 2023-05-18 15:17.
* 
"""
from sys import stdin
def f91(N):
    return f91(f91(N+11)) if N<=100 else N-10
for read in stdin:
    N = int(read)
    if N==0: 
        break
    print(f"f91({N}) = {f91(N)}")
