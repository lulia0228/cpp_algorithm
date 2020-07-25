//
// Created by LiHeng on 2020/6/3.
//

// 345 反转字符串中的元音字母
#include <iostream>
#include <unordered_set>

using namespace std;
class Solution {
public:
    string reverseVowels(string s) {
        if(s == "") return "";
        unordered_set<char> st = {'a','e','i','o','u','A', 'E', 'I', 'O', 'U'};
        int i=0, j=s.size()-1;
        while(i<j){
            if(st.find(s[i]) == st.end())//左边字母不是元音
                ++i;
            else if(st.find(s[j]) == st.end())//右边字母不是元音
                --j;
            else
                swap(s[i++],s[j--]);
        }
        return s;
    }
};