"""
* ZeroJudge f640. 函數運算式求值
* https://zerojudge.tw/ShowProblem?problemid=f640
* Authored by Yang Yu-Chieh at 2023-05-18 15:56.
* 從尾端開始看起，只要遇到數字就推進stack，
* 遇到f,g,h就從stack中pop出需要的數量，
* 最後再將函數運算結果丟回stack中。
"""
from sys import stdin
def f(x):   return 2*x-3
def g(x,y):    return 2*x+y-7
def h(x,y,z):    return 3*x-2*y+z
stk = []
def stk_top():  return stk[-1]
def stk_push(x):    stk.append(x)
def stk_pop():  return stk.pop()

for read in stdin:
    v = reversed(read.split())
    for now in v:
        if now=='f':
            stk_push(f(stk_pop()))
        elif now=='g':
            stk_push(g(stk_pop(), stk_pop()))
        elif now=='h':
            stk_push(h(stk_pop(), stk_pop(), stk_pop()))
        else:
            stk_push(int(now))
    print(stk_pop())

