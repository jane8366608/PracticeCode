"""
* ZeroJudge d071. 格瑞哥里的煩惱 (EOF版)
* https://zerojudge.tw/ShowProblem?problemid=d071
* Authored by Yang Yu-Chieh at 2023-05-16 15:28.
* 
"""
from sys import stdin
for s in stdin:
    s = int(s)
    if s%4==0:
        if s%400!=0 and s%100==0:
            print("a normal year")
        else:
            print("a leap year")
    else:
        print("a normal year")
