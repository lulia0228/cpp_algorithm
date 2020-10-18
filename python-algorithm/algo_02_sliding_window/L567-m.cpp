
#include <iostream>
#include <cstring>
#include <vector>
using namespace std ;


//首先这道题用暴力解法超时

//因此用的是滑动窗口解法
class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int sz1 = s1.size();
        int sz2 = s2.size();
        if (sz1 > sz2) return false;
        vector<int> v1(128, 0);
        vector<int> v2(128, 0);
        for(auto c:s1)
            ++v1[c];
        int l=0;
        for(int r=0; r<sz2; ++r){
            ++v2[s2[r]];
            if(r-l+1 == sz1){
                if (v1 == v2)
                    return true;
                --v2[s2[l]];
                ++l;
            }
        }
        return false;
    }
};


//这种解法是从L76转化过来，不同的是，更新窗口的时机不一样
//L76是当前字符出现了
class Solution1 {
public:
    bool checkInclusion(string s1, string s2) {
        vector<int> chars(128, 0);
        vector<bool> flag(128, false);
        // 先统计T中的字符情况
        for(int i = 0; i < s1.size(); ++i) {
            flag[s1[i]] = true;
            ++chars[s1[i]]; //为了处理s1中重复字母
        }
        // 移动滑动窗口，不断更改统计数据
        int cnt = 0, l = 0;
        for (int r = 0; r < s2.size(); ++r) {
            if (flag[s2[r]]) {
                if (--chars[s2[r]] >= 0)
                    ++cnt;
            }
            // 若目前滑动窗口长度等于s1长度，判断是否是s1的全排列
            if(r-l+1 == s1.size()){
                if (cnt == s1.size())
                    return true;
                if (flag[s2[l]] && ++chars[s2[l]] > 0)
                    --cnt;
                ++l;
            }
        }
        return false;
    }
};

int main(){
    string s1 = "ab";
    string s2 = "eidboaoo";
    cout << Solution().checkInclusion(s1,s2)<<endl;
}