//
// Created by 李恒 on 2020/1/3.
//

// 344 反转字符串

#include <iostream>
#include <cstring>
#include <vector>

using namespace std;

class Solution {
public:
    void reverseString(vector<char>& s) {
        for(int i=0 ;i < s.size()/2; i++)
            swap(s[i],s[s.size()-1-i]);
    }
};