"""
* ZeroJudge a058. MOD3
* https://zerojudge.tw/ShowProblem?problemid=d669
* Authored by Yang Yu-Chieh at 2023-05-16 14:15.
* 。
"""
num = int(input())
k1=k2=k3=0
for i in range(num):
    tmp = int(input())
    if tmp%3==0:
        k3 += 1
    elif tmp%3==1:
        k1 += 1
    else:
        k2 += 1
print(k3, k1, k2)
