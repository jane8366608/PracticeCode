"""
* ZeroJudge e969. 3. 大吃大喝 (Big eater)
* https://zerojudge.tw/ShowProblem?problemid=e969
* Authored by Yang Yu-Chieh at 2023-05-17 00:10.
*  輸入總共有三個整數，以空白隔開。
* 第一個整數 N ( 0 ≤ N ≤ 500 )為 Wayne 總共帶了多少錢，
* 第二個整數 M ( 0 < M ≤ 60 )為他每隔幾分鐘進食一次，
* 第三個 整數 K = 0 的話代表從蘋果派(32)開始吃，
* K = 1 的話則代表從玉米濃湯(55)開始。
"""
N, M, K = map(int, input().split())


    
cnt = 0

while True:
    
    if K==0:
        if N>=32:
            N-=32
        else:
            if cnt ==0:
                print("Wayne can't eat and drink.")
            break
    elif K==1:
        if N>=55:
            N-=55
        else:
            if cnt ==0:
                print("Wayne can't eat and drink.")
            break
    print("%d: Wayne " %(M*cnt), end="")
    cnt+=1
    print("eats an Apple pie" if K==0 else "drinks a Corn soup", end="")
    K = 0 if K==1 else 1
    print(", and now","he has %d dollars." %N if N>1 else ("he has 1 dollar." if N==1 else "he doesn't have money."))
