/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/
// i399. 1. 數字遊戲 2022年6月APCS(第一題)
// https://zerojudge.tw/ShowProblem?problemid=i399

#include <bits/stdc++.h>
using namespace std;

int main()
{
    int i=0, tmp=0, Arr[10]={0};
    for(i=0;i<3;i++){
        cin>>tmp;
        Arr[tmp]++;
    }

    int max_cnt=0;
    for(i=0;i<10;i++){
        if(max_cnt<Arr[i])
            max_cnt=Arr[i];
    }
    cout<<max_cnt<<" ";
    for(i=9;i>0;i--){
        if(Arr[i])
            cout<<i<<" ";
    }
    return 0;
}
