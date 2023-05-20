"""
* ZeroJudge d044. 00640 - Self Numbers
* https://zerojudge.tw/ShowProblem?problemid=d044
* Authored by Yang Yu-Chieh at 2023-05-19 13:48.
* set():無序不重複元素集，可用於消除重複元素。
***a=[1,3,5], b=[1,2,3]
** union():並/聯集(or)  # [1,2,3,5]
* set(a) | set(b)
* set(a).union(b)
** &:交集(and)          # [1,3]
* set(a) & set(b)
* set(a).intersection(b)
** -:差集 (difference)  # [5]
* set(a)-set(b)
* set(a).difference(b)
** ^:對稱差集，返回兩個集合中不重複的元素。 # [2,5]
* set(a)^set(b)
* set(a).symmetric_difference(b)
"""
nmax = 10**6
matA = []
matB = list(range(1,nmax+1))    # 用這種寫法會比[x for x in range(1,nmax)]耗時短
def d(n):
    A = list(map(int, str(n)))    # 用這種寫法會比[int(x) for x in str(x)]耗時短
    tmp = n+sum(A)
    if tmp <= nmax:
        matA.append(tmp)
    # return
for i in range(1,nmax+1):
    d(i)
matA = set(matA) ^ set(matB)
for i in matA:
    print(str(i))
     
