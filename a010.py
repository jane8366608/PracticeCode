"""
* ZeroJudge a010. 因數分解
* https://zerojudge.tw/ShowProblem?problemid=a010
* Authored by Yang Yu-Chieh at 2023-05-16 16:53.
* 
"""
x = int(input())
mat=[]
prime = 2
while(x!=1):
    if x%prime ==0:
        mat.append(prime)
        x /= prime
    else:
        prime += 1
cnt=0

while len(mat)!=0:
    if mat.count(mat[0])>1:
        print("%d^%d" %(mat[0],mat.count(mat[0])),end=" ")
        del mat[:mat.count(mat[0])]
    else:
        print(mat[0], end=" ")
        del mat[0]
    if len(mat)>0:
        print("*", end=" ")
