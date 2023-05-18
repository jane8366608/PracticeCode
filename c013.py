"""
* ZeroJudge c013. 00488 - Triangle Wave
* https://zerojudge.tw/ShowProblem?problemid=c013
* Authored by Yang Yu-Chieh at 2023-05-18 14:24.
* 
"""
from sys import stdin
n = int(input())
input() # 題目特殊要求，用print()不行，不然會有RE
for n in range(n):
    # A振幅(<=9)，F頻率(波的數量)
    A = int(input())
    F = int(input())
    print()
    for i in range(F):
        for j in range(1,A+1):
            print(f"{str(j)*j}" )
        for j in range(A-1,0,-1):
            print(f"{str(j)*j}" )
        print()
            
