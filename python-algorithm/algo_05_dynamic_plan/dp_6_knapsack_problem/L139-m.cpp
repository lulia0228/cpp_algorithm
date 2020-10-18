
#include <iostream>
#include <vector>
#include <algorithm>
//  vector 不同于map（map有find方法），vector本身是没有find这一方法，其find是依靠algorithm来实现的。
// 使用方法 find(vec.begin(), vec.end(), target) 没有返回 vec.end（）
// 不想用find方法，也可以开辟一个 无序集合 用unordered_set自带find
using namespace std;
class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        vector<bool> dp(s.size()+1, false); //dp[i]表示s[0,i) 是否可以拆分成... 这里从1计数，1代表第一个字母
        dp[0] = true;
        for(int i=1; i<=s.size(); ++i){
            for(int j=0; j<i; j++){ //s.substr第二个参数不是代表子串结尾位置，代表的是子串的长度，一开始搞错了，调试很久
                if (dp[j] && find(wordDict.begin(), wordDict.end(), s.substr(j,i-j)) != wordDict.end()){
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[s.size()];
    }
};

int main(){
    string s = "applepenapple";
    vector<string> vec = {"apple","pen"};
    bool res = Solution().wordBreak(s, vec);
    cout << res <<endl;
}