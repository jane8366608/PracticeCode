"""
* ZeroJudge e834. P1.批發出貨(Wholesale)
* https://zerojudge.tw/ShowProblem?problemid=e834
* Authored by Yang Yu-Chieh at 2023-05-16 15:30.
* 
"""
import math
M = int(input())
N = list(map(int, input().split()))
for x in N[:-1]:
    print(x//M if math.ceil(x/M)==x/M else math.ceil(x/M)*M-x)
        
