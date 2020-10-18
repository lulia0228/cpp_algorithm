
/* 滑动窗口双指针一般逻辑
int left = 0, right = 0;
while (right < s.size()) {
    // 增大窗口
    window.add(s[right]);
    right++;

    while (window needs shrink) {
    // 缩小窗口
        window.remove(s[left]);
        left++;
    }
}*/


//思路：借助双指针滑动窗口+哈希表（字典）解决

#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> findAnagrams(string s, string t) {
        unordered_map<char, int> need, window;
        for (char c : t) need[c]++; //t中可能有重复字母

        int left = 0, right = 0;
        int valid = 0; //相同字母计数
        vector<int> res; // 记录结果
        while (right < s.size()) {
            char c = s[right];
            right++;
            // 进行窗口内数据的一系列更新
            if (need.count(c)) {
                window[c]++;
                if (window[c] == need[c])
                    valid++;
            }
            // 判断左侧窗口是否要收缩
            while (right - left >= t.size()) {
                // 当窗口符合条件时，把起始索引加入 res
                if (valid == need.size()) //注意valid个数等于need元素个数，而不是t的长度，考虑重复字母的存在
                    res.push_back(left);
                char d = s[left];
                left++;
                // 进行窗口内数据的一系列更新
                if (need.count(d)) {
                    if (window[d] == need[d])
                        valid--;
                    window[d]--;
                }
            }
        }
        return res;
    }
};


// L76 最小覆盖子串
// L567 判断一个字符串中是否存在子串是另一个字符串的排列
// L3 最长无重复子串 相当于