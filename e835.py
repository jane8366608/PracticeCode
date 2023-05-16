"""
* ZeroJudge e835. p2.表演座位 (Seats)
* https://zerojudge.tw/ShowProblem?problemid=e835
* Authored by Yang Yu-Chieh at 2023-05-16 09:254.
* 
"""
import math
w = int(input())
# 第幾區，一:1~2500、二:2501~7500、三:7501~1000
if w>=1 and w<=2500:
    print("1", math.ceil(w/25),w%25 if w%25!=0 else 25)
elif w>2500 and w<=7500:
    print("2",math.ceil((w-2500)/50),(w-2500)%50 if (w-2500)%50!=0 else 50)
else:
    print("3", math.ceil((w-7500)/25),(w-7500)%25 if (w-7500)%25!=0 else 25)
    

