"""
* ZeroJudge a693. 吞食天地
* https://zerojudge.tw/ShowProblem?problemid=a693
* Authored by Yang Yu-Chieh at 2023-05-18 15:17.
* 為了避免超時 ( TLE )，可以採用下列兩個做法：
* 將「計算總和」放在擷取範圍的迴圈之外，
* 就不需要每次執行迴圈時都計算一次總和。
* 透過 Python 的標準函式庫「高效迭代器 itertools」計算總和。
* 計算出總和後，
* 如果要計算 a~b 範圍內的數值，
* 只需要用 0~b 的總和，
* 減去 0~a-1 的總和，就可以得到最後的結果。
"""
from sys import stdin
from itertools import accumulate 
for read in stdin:
    n, m = map(int, read.split())
    mat = list(map(int, input().split()))
    sum_mat = [0]+list(accumulate(mat))
    for i in range(m):
        l, r = map(int, input().split())
        print(sum_mat[r]-sum_mat[l-1])
