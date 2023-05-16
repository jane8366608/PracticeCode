"""
* ZeroJudge c022. 10783 - Odd Sum
* https://zerojudge.tw/ShowProblem?problemid=c022
* Authored by Yang Yu-Chieh at 2023-05-16 14:46.
* 總和梯形公式=(a+b)*數量/2=(a+b)*((b-a)/2+1)/2=(b^2-a^2)/4+(a+b)/2。
"""
T = int(input())
for i in range(T):
    a = int(input())
    b = int(input())
    if a%2==0:
        a += 1
    if b%2==0:
        b -= 1
    print("Case %d: %d" %(i+1,(b**2-a**2)/4+(a+b)/2))
