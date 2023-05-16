"""
* ZeroJudge d010. 盈數、虧數和完全數
* https://zerojudge.tw/ShowProblem?problemid=d010
* Authored by Yang Yu-Chieh at 2023-05-16 15:48.
* 
"""
from sys import stdin
for s in stdin:
    s = int(s)
    p = 0
    for i in range(1,s):
        if s%i==0:
            p += i
    print("盈數" if p>s else ("虧數" if p<s else "完全數"))
