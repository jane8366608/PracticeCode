"""
* ZeroJudge d072.格瑞哥里的煩惱 (Case 版)
* https://zerojudge.tw/ShowProblem?problemid=d069
* Authored by Yang Yu-Chieh at 2023-05-16 09:25.
* 閏年公式：除了"不是400"的倍數和"100"的倍數以外，四的倍數的年份均為閏年。
"""
a = int(input())
for i in range(a):
    s = int(input())
    if s%4==0:
        if s%100==0 and s%400!=0:
            print("Case %d: a normal year" %(i+1))
        else:
            print("Case %d: a leap year" %(i+1))
    else:
        print("Case %d: a normal year" %(i+1))
