//
// Created by 李恒 on 2020/7/1.
//

#include <iostream>
#include <cstring>
#include <vector>
using namespace std;

//2 记录一个字符上次出现的位置，如果两个字符串中的字符上次出现的位置一样，那么就属于同构。

class Solution1 {
public:
    bool isIsomorphic(string s, string t) {
        vector<int> preIndexOfS(256,0);
        vector<int> preIndexOfT(256,0);
        for (int i = 0; i < s.size(); i++) {
            if (preIndexOfS[s[i]] != preIndexOfT[t[i]]) {
                return false;
            }
            preIndexOfS[s[i]] = i + 1;
            preIndexOfT[t[i]] = i + 1;
        }
        return true;
    }
};

//我的解法：最后个案例没通过，不知道为啥
class Solution {
public:
    bool isIsomorphic(string s, string t) {
        return convert2num(s) == convert2num(t);
    }

    string convert2num(string str){
        int index = 1;
        char c = str[0];
        string res = "1";
        for(int i=1; i<str.size(); ++i){
            if(str[i] != c){
                ++index;
                c = str[i];
            }
            res += to_string(index);
        }
        return res;
    }
};