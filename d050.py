# d050. 妳那裡現在幾點了？
# https://zerojudge.tw/ShowProblem?problemid=d050
T = int(input())
# if寫法
# if T >=15 :
#     print(T-15)
# elif T<15 :
#     print(T-15+24)
print((9+T)%24)
