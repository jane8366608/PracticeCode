"""
* ZeroJudge c002. 10696 - f91
* https://zerojudge.tw/ShowProblem?problemid=c002
* Authored by Yang Yu-Chieh at 2023-05-18 15:17.
* 按照它的遞迴規則可以發現，
* 只要輸入的N大於100則只需要算一次就有答案，
* 即N-10；
* 而N小於101時不管N是多少，
* 跑到最後都會進入101~111的數字，
* 不論是這之中的哪一個數字，
* 最後都會進入101→91，
* 所以解這題只需O(1)。
"""
from sys import stdin
def f91(N):
    return f91(f91(N+11)) if N<=100 else N-10
for read in stdin:
    N = int(read)
    if N==0: 
        break
    print(f"f91({N}) = {f91(N)}")
