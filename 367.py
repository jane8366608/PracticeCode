"""
* ZeroJudge b367. 翻轉世界
* https://zerojudge.tw/ShowProblem?problemid=b367
* Authored by Yang Yu-Chieh at 2023-05-18 13:48.
* 矩陣倒轉後比對
"""
from sys import stdin
T = int(input())
for k in range(T):
    # N長，M寬 (0~11(不含))
    N, M = map(int, input().split())
    mat = []
    for i in range(N):
        mat.append(list(map(int,input().split())))

    new = []
    for i in range(N-1,-1,-1):
        new.append([mat[i][j] for j in range(M-1,-1,-1)])
    
    print("go forward" if mat==new else "keep defending")
        
            
    
    
        
    
