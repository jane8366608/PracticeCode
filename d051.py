# d051. 糟糕，我發燒了！
# https://zerojudge.tw/ShowProblem?problemid=d051
# 攝氏溫度*9/5+32 = 華氏溫度
# 攝氏溫度 = (華氏溫度-32)*5/9
F = float(input())
C = (F-32)*5/9
print("%.3f" %C)
