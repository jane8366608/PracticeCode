"""
* ZeroJudge e969. 3. 大吃大喝 (Big eater)
* https://zerojudge.tw/ShowProblem?problemid=e969
* Authored by Yang Yu-Chieh at 2023-05-17 00:10.
*  
"""
from sys import stdin
for s in stdin:
    n, k = map(int, s.split())
    cnt = n
    while True:
        cnt += n//k
        if n//k+n%k<k:
            break
        n = n//k+n%k
    print(cnt)
        
