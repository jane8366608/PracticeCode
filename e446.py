"""
* ZeroJudge e446. 排列生成
* https://zerojudge.tw/ShowProblem?problemid=e446
* Authored by Yang Yu-Chieh at 2023-05-18 15:56.
* 從尾端開始看起，只要遇到數字就推進stack，
* 遇到f,g,h就從stack中pop出需要的數量，
* 最後再將函數運算結果丟回stack中。
"""
from sys import stdin,stdout
from itertools import permutations
for N in stdin:
    tmp = [str(x) for x in range(1, int(N)+1)]
    p = permutations(tmp)
    for x in p:
        stdout.write(' '.join(x)+'\n')  
