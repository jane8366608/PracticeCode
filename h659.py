# h659. 計程車 (Taxi)
# https://zerojudge.tw/ShowProblem?problemid=h659
K, W, S, E = input().split()
K, W, S, E = int(K), int(W), int(S), int(E)
cnt = 0
# K:行駛總公里數，計程運價:起程 2 公里內皆為 20 元,續程每滿 1 公里加 5 元。
cnt += 20 + max(0, K-2)*5
# print("1 cnt = ", cnt)
# W:車輛延滯時間，延滯計時運價:延滯時間每滿 2 分鐘加 5 元。
cnt += W//2*5
# print("2 cnt = ", cnt)
# S:該次乘載的乘客上車的時間點。
# E:該次乘載的乘客下車的時間點。

if E <= 18: # 沒有觸發夜間加成運價
    print(cnt)
else:   # 觸發夜間加成運價
    """
    晚間 18 時至 19 時 185 元
    晚間 19 時至 20 時 195 元
    晚間 20 時至 21 時 205 元
    晚間 21 時至 22 時 215 元
    晚間 22 時至 23 時 225 元
    """
    if S < 18:
        S=18
    print(int(cnt+(185+10*(S-18))*(E-S)+10*(E-S)*(E-S-1)/2))

    
