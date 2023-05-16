"""
* ZeroJudge d669. 11677 - Alarm Clock
* https://zerojudge.tw/ShowProblem?problemid=d669
* Authored by Yang Yu-Chieh at 2023-05-16 14:05.
* 都換成分，再做判斷處理。
"""
from sys import stdin
for s in stdin:
    h1,m1,h2,m2 = map(int, s.rstrip().split())
    if h1==0 and m1==0 and h2==0 and m2==0:
        break
    t1 = h1*60+m1
    t2 = h2*60+m2
    print(1440-t1+t2 if t1>t2 else t2-t1)

