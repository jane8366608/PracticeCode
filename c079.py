"""
* ZeroJudge c079. 10346 - Peter's Smokes
* https://zerojudge.tw/ShowProblem?problemid=c079
* Authored by Yang Yu-Chieh at 2023-05-17 8:00.
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
        
