"""
* ZeroJudge c005. 10300 - Ecological Premium
* https://zerojudge.tw/ShowProblem?problemid=c005
* Authored by Yang Yu-Chieh at 2023-05-16 14:31.
* 農夫農場的面積/農場裡動物的數目*環保等級*農場裡動物的數目=農夫農場的面積*環保等級。
"""
n = int(input())
for i in range(n):
    f = int(input())
    mat = []
    for j in range(f):
        mat.append([int(x) for x in input().split()])
    p=0
    for j in range(f):
        p += mat[j][0]*mat[j][2]
    print(p)
    
    
