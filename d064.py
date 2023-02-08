# d064. ㄑㄧˊ 數？
# https://zerojudge.tw/ShowProblem?problemid=d064
i = int(input())

if i%2 == 0 :
    print("Even")
else:
    print("Odd")

# 也可以這樣寫
print("Odd" if i%2 else "Even")
