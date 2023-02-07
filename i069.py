# i069. 岩石觀察 (Stones)
# https://zerojudge.tw/ShowProblem?problemid=i069
N = int(input())
X = list(map(int, input().split()))
avg = int(sum(X)/N)
_MAX, _min = max(X), min(X)
_MAXIndex, _minIndex = X.index(_MAX), X.index(_min) 
# cost = _MAX - avg
X[_MAXIndex], X[_minIndex] = avg, _min + _MAX - avg
for i in X:
    print(i, end = " ")
