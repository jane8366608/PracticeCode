"""
* ZeroJudge d189. 11150 - Cola
* https://zerojudge.tw/ShowProblem?problemid=d189
* Authored by Yang Yu-Chieh at 2023-05-17 14:56.
* "3瓶空可樂罐換一瓶可樂"代表每換一次瓶子的數量減少2，
* 而實際喝的可樂數增加1，所以最終答案等於N+換的次數。
  能借罐子      不能借罐子
空罐    能換次數    空罐    能換次數
3       1           3       1
6       3           6       2
9       4           9       4
12      5           12      5
15      7           15      7
18      9           18      8
N       N//2        N       (N-1)//2

可喝可樂數=N+能換次數=N+N//2=N*3//2
"""
from sys import stdin
for N in stdin:
    N = int(N)
    print(N+N//2)
    
    
