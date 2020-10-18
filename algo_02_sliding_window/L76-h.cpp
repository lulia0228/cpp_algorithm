
// 滑动窗口思想
#include <iostream>
#include <cstring>
#include <vector>
using namespace std;

class Solution {
public:
    string minWindow(string s, string t) {
        vector<int> chars(128, 0);
        vector<bool> flag(128, false);
        vector<int> record(128, 0);
        // 先统计T中的字符情况
        for(int i = 0; i < t.size(); ++i) {
            flag[t[i]] = true;
            ++chars[t[i]]; //为了处理t中重复字母
        }
        // 移动滑动窗口，不断更改统计数据
        int cnt = 0, l = 0, min_l = 0, min_size = s.size() + 1;
        for (int r = 0; r < s.size(); ++r) {
            if (flag[s[r]]) {
                ++record[s[r]];
                // 若目前滑动窗口已包含T中全部字符，
                // 则尝试将l右移，在不影响结果的情况下获得最短子字符串
                //条件是record中字母频次要≥chars中字母频次
                while (IsIntend(chars, record)) {
                    if (r - l + 1 < min_size) {
                        min_l = l;
                        min_size = r - l + 1;
                    }
                    if (flag[s[l]]) {
                        --record[s[l]];
                    }
                    ++l;
                }
            }
        }
        return min_size > s.size()? "": s.substr(min_l, min_size);
    }

    bool IsIntend(vector<int>& v1, vector<int>& v2){
        for(int i=0; i<128; ++i){
            if (v1[i] > v2[i])
                return false;
        }
        return true;
    }

};

//上面解法在leetcode上速度比较慢160ms，速度慢是因为对2个哈希表做了比较导致的
//下面的解法之所以快，是因为设计了一个cnt变量来代表目前窗口中所有t中字母都出现，就算重复也是

//这种设计很巧妙 cnt计数 时间16ms
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
    string res = Solution().minWindow(s, t);
    cout << res <<endl;
}

//209. 长度最小的子数组
//904. 水果成篮（Python3）
//930. 和相同的二元子数组（Java，Python）
//992. K 个不同整数的子数组滑动窗口（Python）
//1004. 最大连续 1 的个数 III滑动窗口（Python3）
//1248. 统计「优美子数组」滑动窗口（Python）
