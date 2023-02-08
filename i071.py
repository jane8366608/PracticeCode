# i071. 風景 (Landscape)
# https://zerojudge.tw/ShowProblem?problemid=i071
N, M = input().split()
N, M = int(N), int(M)
T = list(map(int, input().split()))
T.insert(0,0)
#  原屋左面
# print("原屋左面")
# print(T)
cnt = 0
leftMAX = T[M]
for i in range(M-1,-1,-1):
    # print("leftMAX = %d, compare = %d"%(leftMAX,T[i]))
    if T[i] > leftMAX:
        # print("tmp = %d, compare = %d"%(tmp,T[j]), end = "\t")
        cnt += 1
        leftMAX = T[i]
        # print(T)
    
# 原屋右面
# print("原屋右面")
# print(T)
rightMAX = T[M]
for i in range(M+1, N+1):
    # print("rightMAX = %d, compare = %d"%(rightMAX,T[i]))
    if T[i] > rightMAX:
        cnt += 1
        rightMAX = T[i]
print(cnt)  
