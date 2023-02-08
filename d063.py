# d063. 0 與 1
# https://zerojudge.tw/ShowProblem?problemid=d063
m = int(input())
# if解法
if m :
    print(0)
else:
    print(1)

# 不需要if的解法
# XOR(^):不同才是1, 1^1 = 0, 0^1 = 1 
print(m^1)
