# e968. 2. 班級名單 (Student list)
# https://zerojudge.tw/ShowProblem?problemid=e968
N = int(input())
a = list(map(int, input().split()))
for i in range(N,0,-1):
    if i not in a:
        print("No.", i)
