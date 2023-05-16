"""
* ZeroJudge a015.矩陣的翻轉
* https://zerojudge.tw/ShowProblem?problemid=a015
值  i   j   i'  j'
---------------------
3   0   0   0   0
1   0   1   1   0
2   0   2   2   0
8   1   0   0   1
5   1   1   1   1  
4   1   2   2   1
=> 觀察得到結論：i,j互換。
"""
from sys import stdin

for s in stdin:
    r, c = map(int, s.rstrip().split()) # 讀入r和c，並類型轉換。
    matrix = []
    for i in range(r):  # r rows
        matrix.append([int(x) for x in input().split()])    # 一次讀一行，將之切割成各元素置入串列中
    
    # 直接i, j互換輸出。
    for i in range(c):  # c rows
        for j in range(r): # r columns
            print(matrix[j][i], end=" ")
        print()
        
    
