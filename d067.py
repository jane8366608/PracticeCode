"""
* ZeroJudge d067.格瑞哥裡的煩惱(1行版)
* https://zerojudge.tw/ShowProblem?problemid=d067
* Authored by Yang Yu-Chieh at 2023-05-16 08:58.
* 閏年公式：除了"不是400"的倍數和"100"的倍數以外，四的倍數的年份均為閏年。
"""
from sys import stdin
for s in stdin:
    s = int(s)
    if s%4==0:  # 是4的倍數
        if s%100==0 and s%400!=0:    # 是100或400的倍數
            print("a normal year")
        else:
            print("a leap year")
    else:
        print("a normal year")
