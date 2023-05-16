"""
* ZeroJudge a148. You Cannot Pass?!
* https://zerojudge.tw/ShowProblem?problemid=a148
* Authored by Yang Yu-Chieh at 2023-05-16 15:41.
* 
"""
from sys import stdin
for s in stdin:
    grade = list(map(int, s.split()))
    print("no" if sum(grade[1::])/grade[0]>59 else "yes")
