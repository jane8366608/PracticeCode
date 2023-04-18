// i428. 1. 巴士站牌 2022年10月APCS
// https://zerojudge.tw/ShowProblem?problemid=i428

#include <iostream>

using namespace std;

int main()
{
    int i=0, j=0 ,n=0;
    int Arr[100][2];
    cin>>n;
    // Arr初始化值為-999
    for(i=0;i<100;i++)
        for(j=0;j<2;j++)
            Arr[i][j]=-999;
    // 讀入巴士站的座標
    for(i=0;i<n;i++)
        for(j=0;j<2;j++)
            cin>>Arr[i][j];
        
    
    // 計算相鄰兩站的曼哈頓距離 |X1-X2| + |Y1-Y2|
    int dis=0,max_dis=-9999, min_dis=9999;
    for(i=0;i<n-1;i++){
        dis = abs(Arr[i+1][0]-Arr[i][0])+abs(Arr[i+1][1]-Arr[i][1]);
        if (dis>max_dis)
            max_dis=dis;
        if (dis<min_dis)
            min_dis=dis;
    }
    cout<<max_dis<<" "<<min_dis<<endl;
    return 0;
}
