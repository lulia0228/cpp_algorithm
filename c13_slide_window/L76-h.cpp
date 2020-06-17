//
// Created by LiHeng on 2020/6/4.
//

#include <iostream>
#include <cstring>
#include <unordered_map>
using namespace std;

class Solution {
public:
    string minWindow(string s, string t) {
        unordered_map<char,int> mp_t;
        unordered_map<char,int> mp_s;
        // 先统计T中的字符情况
        for(int i = 0; i < t.size(); ++i)
            mp_t[t[i]]++;
        // 移动滑动窗口，不断更改统计数据
        int l = 0, min_l = 0, min_size = s.size()+1;
        for (int r = 0; r < s.size(); ++r) {
            if (mp_t.find(s[r]) != mp_t.end()) {
                mp_s[s[r]]++;
                while(isContent(mp_s, mp_t)){
                    if (mp_t.find(s[l]) != mp_t.end()){
                        if(r-l+1 < min_size){
                            min_l = l;
                            min_size = r-l+1;
                        }
                        mp_s[s[l]]--;
                    }
                    ++l;
                }
            }
        }
        return min_size > s.size()? "": s.substr(min_l, min_size);
    }

    bool isContent(unordered_map<char,int> m1, unordered_map<char,int> m2){
        if(m1.size() != m2.size())
            return false;
        for(auto item:m1){
            if(item.second < m2[item.first])
                return false;
        }
        return true;
    }
};
//上面解法在leetcode上最后一个长测试案例没通过，速度慢是因为我对两个字典进行比较造成的
//下面的解法之所以快，是因为设计了一个cnt变量来代表目前窗口中所有t中字母都出现，就算重复也是

//重要理解： chars 表示目前每个字符缺少的数量，flag 表示每个字符是否在 T 中存在。
#include <vector>
class Solution1 {
public:
    string minWindow(string s, string t) {
        vector<int> chars(128, 0);
        vector<bool> flag(128, false);
        // 先统计T中的字符情况
        for(int i = 0; i < t.size(); ++i) {
            flag[t[i]] = true;
            ++chars[t[i]]; //为了处理t中重复字母
        }
        // 移动滑动窗口，不断更改统计数据
        int cnt = 0, l = 0, min_l = 0, min_size = s.size() + 1;
        for (int r = 0; r < s.size(); ++r) {
            if (flag[s[r]]) {
                if (--chars[s[r]] >= 0) {
                    ++cnt;
                }
                // 若目前滑动窗口已包含T中全部字符，
                // 则尝试将l右移，在不影响结果的情况下获得最短子字符串
                while (cnt == t.size()) {
                    if (r - l + 1 < min_size) {
                        min_l = l;
                        min_size = r - l + 1;
                        //cout << s.substr(min_l, min_size)<<endl;
                    }
                    if (flag[s[l]] && ++chars[s[l]] > 0) {
                        --cnt;
                    }
                    ++l;
                }
            }
        }
        return min_size > s.size()? "": s.substr(min_l, min_size);
    }
};

int main(){
    string s = "ADOBECODEBANC";
    string t = "ABC";
    string res = Solution1().minWindow(s, t);
    cout << res <<endl;
}

//209. 长度最小的子数组
//904. 水果成篮（Python3）
//930. 和相同的二元子数组（Java，Python）
//992. K 个不同整数的子数组滑动窗口（Python）
//1004. 最大连续 1 的个数 III滑动窗口（Python3）
//1248. 统计「优美子数组」滑动窗口（Python）
