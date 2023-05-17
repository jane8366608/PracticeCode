"""
* ZeroJudge d053. 10970 - Big Chocolate
* https://zerojudge.tw/ShowProblem?problemid=d053
* Authored by Yang Yu-Chieh at 2023-05-17 13:20.
* 每一刀都會一個大塊分成兩個小塊

* 這些小塊如果不是一小塊(1*1單位的巧克力) 也是當成一個大塊繼續切成兩小塊

* 所以就是答案就是所有塊數-1
"""
from sys import stdin
for s in stdin:
    M, N = map(int, s.split())
    print(N*M-1)
