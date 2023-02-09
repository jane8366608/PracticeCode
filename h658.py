# h658. 捕魚 (Fishing)
# https://zerojudge.tw/ShowProblem?problemid=h658
X, Y = input().split()
X, Y = int(X), int(Y)
N = int(input())

dist = 9999999
minA, minB = 0, 0
for i in range(N):
    A, B = input().split()
    A, B = int(A), int(B)
    tmp = ((X-A)**2+(Y-B)**2)**0.5
    # print("dist = %f, tmp = %f" %(dist, tmp), end = " ")
    if dist > tmp:
        dist = tmp
        minA, minB = A, B
        # print("minA = %d, minB = %d, dist' = %f" %(minA, minB, dist))
print(minA, minB)
