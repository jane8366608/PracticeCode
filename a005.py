"""
* ZeroJudge a005. Eva 的回家作業
* https://zerojudge.tw/ShowProblem?problemid=005
* Authored by Yang Yu-Chieh at 2023-05-16 14:22.
* 判斷是等差還是等比。
"""
t = int(input())
for i in range(t):
    a = [int(x) for x in input().split()]
    for j in range(4):
        print(a[j], end=" ")
    print(a[3]+a[2]-a[1] if a[3]-a[2] == a[2]-a[1] else a[3]*a[2]//a[1])
