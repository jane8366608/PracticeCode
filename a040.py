"""
* ZeroJudge a040. 阿姆斯壯數
* https://zerojudge.tw/ShowProblem?problemid=a040
* Authored by Yang Yu-Chieh at 2023-05-18 14:40.
* 
"""
from sys import stdin
def arm(N):
    ans = 0
    tmp=N
    N = str(N)
    L=len(N)
    for i in N:
        ans += int(i)**L
    if ans==tmp:
        return True
    return False

for read in stdin:
    n, m = map(int,read.split())
    mat = []
    for i in range(n,m+1):
        if arm(i):
            mat.append(i)
    if len(mat)!=0:
        for x in mat:
            print(x, end=" ")
        print()
    else:
        print("none")
