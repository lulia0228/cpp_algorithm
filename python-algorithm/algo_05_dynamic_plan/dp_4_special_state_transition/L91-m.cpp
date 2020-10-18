

#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    int numDecodings(string s) {
        //先判断能否解码: (1)0开头的不行 （2）0字符前面的数字大于2 （3）连续出现0个数大于1
        for(int i=0; i<s.size(); ++i){
            if(s[i] == '0'){
                if(i==0 || (s[i-1]-'0')>2)
                    return 0;
                int count = 0; //下面循环执行了一次当前，所以count 为0
                while(i<s.size() && s[i] == '0'){
                    i++;
                    count++;
                }
                if(count>1)
                    return 0;
            }
        }

        //再用动态规划做（分三种情况）
        int dp[s.size()+1];
        dp[0] = 1;//空也是一种解码方法
        dp[1] = 1;
        for(int i=2; i<= s.size(); ++i){
            //先分支当前元素是否为0
            if(s[i-1] == '0'){ //这里对应dp[i]代表s[0,i)的解码方法种类，i-1是考察的当前元素。
                dp[i] = dp[i-2];
            }
            else{
                int tmp_num = (s[i-2]-'0')*10 + (s[i-1]-'0');
                if(tmp_num <= 26 && tmp_num >= 10)
                    dp[i] = dp[i-1]+dp[i-2];
                else
                    dp[i] = dp[i-1];
            }
        }
        return dp[s.size()];
    }
};