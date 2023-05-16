"""
* ZeroJudge c067. 00591 - Box of Bricks
* https://zerojudge.tw/ShowProblem?problemid=c067
* Authored by Yang Yu-Chieh at 2023-05-16 16:37.
* 也就是計算(大於平均值的數-平均值)的總和。
"""
from sys import stdin
cnt = 1
for n in stdin:
    n = int(n)
    if n==0:
        break
    mat = list(map(int, input().split()))
    avgH = sum(mat[::])//n
    mat = [x-avgH for x in mat]
    p = 0
    for i in mat:
        if i>0:
            p += i
    print("Set #%d\nThe minimum number of moves is %d." %(cnt, p))
    cnt += 1     
    
    
