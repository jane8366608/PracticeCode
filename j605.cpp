# j605. 1. 程式考試 2023年1月APCS
# https://zerojudge.tw/ShowProblem?problemid=j605

/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
using namespace std;

int main()
{
    int i=0, j=0 ,K=0;
    int error=0, max_score=-99, max_time=-99,score=0;
    int Arr[6][2];
  // 初始化陣列值為-2
    for(i=0;i<6;i++)
        for(j=0;j<2;j++)
            Arr[i][j]=-2;
  
    cin>>K;
  // 讀入陣列值
    for(i=0;i<K;i++){
        for(j=0;j<2;j++){
            cin>>Arr[i][j];
        }
    }
  // 找出最高分與嚴重錯誤(-1)。
    for(i=0;i<K;i++){
        if(Arr[i][1]>max_score){
            max_score = Arr[i][1];
            max_time = Arr[i][0];
        }
        if(Arr[i][1]==-1){
            error++;
        }
    }
  // 總分計算 = 提交紀錄中的最高分 - 總提交次數 - 總嚴重錯誤次數 * 2
    score = max_score - K - error*2;
  // 若計算出來的分數為負數則計為0。
    if(score<0)
        score = 0;
    cout<<score<<" "<<max_time<<endl;

    return 0;
}
