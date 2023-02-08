# d060. 還要等多久啊？
# https://zerojudge.tw/ShowProblem?problemid=d060
m = int(input())
# if解法
# m:0~25，需要25-m分
if m <= 25 :
    print(25-m)
# m:26~59，需要60-m+25=85-m分
else:
    print(85-m)


# 不需要if的解法
# m:0~25，需要25-m分 => (25%60+60%60)-m = (85-m)%60
# m:26~59，需要60-m+25=85-m分
print((85-m)%60)
