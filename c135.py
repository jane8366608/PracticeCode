"""
* ZeroJudge c135. 00706 - LC-Display
* https://zerojudge.tw/ShowProblem?problemid=c135
* Authored by Yang Yu-Chieh at 2023-05-17 23:42.
* 
"""
from sys import stdin
# 0表沒橫線，1表有橫線，2表'| '，3表'| |'，4表' |'
#    0 1 2 3 4 5 6 7 8 9
a = [1,0,1,1,0,1,1,1,1,1]
b = [3,4,4,4,3,2,2,4,3,3]
c = [0,0,1,1,1,1,1,0,1,1]
d = [3,4,2,4,4,4,3,4,3,4]
e = [1,0,1,1,0,1,1,0,1,1]
h = {0:" ", 1:"-"}
space = " "
for S in stdin:
    n = S.split()
    s = int(n[0])
    del n[0]
    n = n[0]
    n = list(map(int, n))
    if s==0 and n[0]==0:
        break
    
    
    # 第一排(a)
    for i in n:
        print(f" {h[a[i]]*s} ", end = " ")
    print()
    
    # 第二排(b)
    for i in range(s):
        for j in n:
            if b[j]==2:
                print(f"| {space*s}",end = " ")
            elif b[j]==3:
                print(f"|{space*s}|",end=" ")
            elif b[j]==4:
                print(f"{space*s} |",end=" ")
        print()
    
    # 第三排(c)
    for i in n:
        print(f" {h[c[i]]*s} ", end = " ")
    print()
    
    # 第四排(d)
    for i in range(s):
        for j in n:
            if d[j]==2:
                print(f"| {space*s}",end = " ")
            elif d[j]==3:
                print(f"|{space*s}|",end=" ")
            elif d[j]==4:
                print(f"{space*s} |",end=" ")
        print()
    
    # 第五排(e)
    for i in n:
        print(f" {h[e[i]]*s} ", end = " ")
    print()
        
        
    
