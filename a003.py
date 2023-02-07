# a003. 兩光法師占卜術
# https://zerojudge.tw/ShowProblem?problemid=a003
M, D = input().split()
M, D = int(M), int(D)
S = (M*2+D)%3
if S == 0:
    print("普通")
elif S == 1:
    print("吉")
else:
    print("大吉")
