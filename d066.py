"""
* ZeroJudge d066. 上學去吧！
* https://zerojudge.tw/ShowProblem?problemid=d066
* Authored by Yang Yu-Chieh at 2023-05-16 13:52.
* 先換成分，再做判斷。
"""
h, m = map(int, input().split())
t = 60*h+m
# 7:30-0:00=0:450，17:00-0:00=0:1020
# 若t介於450到1020間，表示必須在校時間。
print("At School" if t>=450 and t<1020 else "Off School")
