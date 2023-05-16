"""
* ZeroJudge a147. Print it all
* https://zerojudge.tw/ShowProblem?problemid=a147
* Authored by Yang Yu-Chieh at 2023-05-16 23:59.
* 大於 0、整數、不可以被 7 整除、小於 n，請輸出所有可能的數字。
"""
from sys import stdin
for s in stdin:
    s = int(s)
    if s==0:
        break
    for i in range(1,s):
        if i%7!=0:
            print(i, end =" ")
    print()
    
