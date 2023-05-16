"""
* ZeroJudge e511. 11364 - Parking
* https://zerojudge.tw/ShowProblem?problemid=e511
* Authored by Yang Yu-Chieh at 2023-05-16 15:05.
* 題意看不懂，但從答案推論就是將整數位置排序後，答案=2*(最大-最小)
"""

t = int(input())
for i in range(t):
    input()
    mat=list(map(int,input().split()))
    mat.sort()
    print(2*(mat[-1]-mat[0]))
    
