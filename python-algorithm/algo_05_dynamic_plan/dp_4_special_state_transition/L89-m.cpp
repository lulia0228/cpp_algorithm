
//格雷编码，动态规划解

//由n位推导n+1位结果时，n+1位结果包含n位结果，同时包含n位结果中在高位再增加一个位1所形成的另一半结果，
// 但是为了保证格雷编码要求的2个连续数值只能有一个二进制位不一样，需要这一半结果和前一半结果镜像排列，即倒过来。
#include <iostream>
#include <vector>

using namespace std;
class Solution {
public:
    vector<int> grayCode(int n) {
        vector<int> res(1, 0);
        for (int i=1 ;i <= n ; i++){
            int e =  1 << i - 1; //每轮循环，一轮循环考察一个二进制位，最高位前加1
            for(int j = res.size()-1; j>=0 ; j--)
                res.push_back(e + res[j]); //按镜像的顺序添加进去
        }
        return res;
    }
};



