'''
d221. 10954 - Add All
* https://zerojudge.tw/ShowProblem?problemid=d221
* Authored by Yang Yu-Chieh at 2023-05-28 13:52.
'''
fin = open(r'C:\\Users\\jane8\Downloads\\.vscode\\P\\test.txt','r', encoding="utf-8")
fout = open(r'C:\\Users\\jane8\Downloads\\.vscode\\P\\result.txt','w', encoding="utf-8")
# print(fin.readlines())
lines = fin.readlines()
A = []
for line in lines:
    A.append(list(map(int,line.rstrip().split())))
index=0

while True:
    if A[index][0]==0:
        break
    cost = []
    index += 1

    tmp = A[index]
    for i in range(len(tmp)-1):
        tmp.sort()
        min1, min2 = tmp[0], tmp[1]
        del tmp[1], tmp[0]
        cost.append(min1+min2)
        tmp.append(min1+min2)

    print(sum(cost), file=fout)
#     index += 1
fin.close()
fout.close()
    
'''鍵盤讀入版本(AC (8.7s, 6.8MB))'''
from sys import stdin

for line in stdin:
    cost = []
    if int(line)==0:
        break
    A = list(map(int, input().rstrip().split()))
    # print(A)
    lenA = len(A)-1
    for i in range(lenA):
        A.sort()
        tmp1, tmp2 = A[0], A[1]
        cost.append(tmp1+tmp2)
        A.append(tmp1+tmp2) 
        del A[1], A[0]
    print(sum(cost))
    
'''heapq版本(AC (0.2s, 7.3MB) )'''
from sys import stdin
import heapq
for line in stdin:
    if int(line)==0:
        break
    A = list(map(int, input().rstrip().split()))
    heapq.heapify(A)
    lenA = len(A)-1
    cost = []
    for i in range(lenA):
        tmp = heapq.heappop(A)+heapq.heappop(A)
        # print(tmp)
        cost.append(tmp)
        heapq.heappush(A,tmp)
    print(sum(cost))
        
               
        

       
    
    
        
    
