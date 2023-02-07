# i070. 比對卡片 (Match)
# https://zerojudge.tw/ShowProblem?problemid=i070
N = int(input())
T = list(map(int, input().split()))
C = list(map(int, input().split()))
Answer = []
for i in range(N):
    tmp = N+1
    for j in range(N):
        if T[i] == C[j]:
            if tmp > abs(i-j):
               tmp = abs(i-j)
    if tmp == N+1:
        Answer.append(-1)
    else:
        Answer.append(tmp)
for i in Answer:
    print(i, end = " ") 
