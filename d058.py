# d058. BASIC 的 SGN 函數
# https://zerojudge.tw/ShowProblem?problemid=d058
n = int(input())
# if解法
if n > 0:
    print("1")
elif n == 0:
    print("0")
else:
    print("-1")

# 不需要if的解法
# 正數印出1 => n/n
# 負數印出-1 => n/abs(n)
# 除數不得為0，所以當n=0時，除數需要為1，用max(n,1)
# 又考慮max(-3,1) = 1，所以應為max(abs(n),1)
print(int((n/max(abs(n),1))))
