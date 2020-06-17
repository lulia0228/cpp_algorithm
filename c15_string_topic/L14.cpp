//
// Created by 李恒 on 2020/1/3.
//

// 14 最长公共前缀

#include <iostream>
#include <cstring>
#include <vector>
using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if(strs.size() == 0)
            return "";
        string res_str = "";

        int tem_s = strs[0].size();
        for(int i=1 ;i < strs.size();i++){
            if (strs[i].size() > tem_s)
                tem_s = strs[i].size();
        }

        for(int i=0; i<tem_s;i++){
            char tem_str = strs[0][i];
            bool flag = true ;
            for(int j=1 ;j < strs.size();j++){
                if (strs[j][i] != tem_str){
                    flag = false;
                    break;
                }
            }
            if(flag)
                res_str += tem_str;
            else
                break;
        }
        return res_str;
    }
};