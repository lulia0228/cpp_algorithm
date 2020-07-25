//
// Created by LiHeng on 2020/6/3.
//

//通过删除字母匹配到字典里最长单词, 如果有多个相等长度的符合要求，返回字典序最小的那个

#include <iostream>
#include <cstring>
#include <vector>

using namespace std;
class Solution {
public:
    string findLongestWord(string s, vector<string>& d) {
        string res = "";
        for(string dd : d){
            int l1 = res.size();
            int l2 = dd.size();
            if(l1 > l2)
                continue;
            if(isSubstr(s, dd)){
                if(l1 < l2 || (l1 == l2 && res > dd))
                    res = dd;
            }
        }
        return res;
    }

    bool isSubstr(string s, string t){
        int j=0;
        for(int i=0; i<s.size(); ++i){
            if(s[i] == t[j])
                ++j;
        }
        return j==t.size();
    }
};