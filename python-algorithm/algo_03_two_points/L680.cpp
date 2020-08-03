//
// Created by LiHeng on 2020/6/3.
//
#include <iostream>
#include <cstring>
using namespace std;
class Solution {
public:
    bool validPalindrome(string s) {
        int i=0, j=s.size()-1;
        for( ; i<j; ++i,--j){
            if(s[i] != s[j])
                return IsPalinSub(s, i+1, j)||IsPalinSub(s, i, j-1);
        }
        return true;
    }

    bool IsPalinSub(string s, int i, int j){
        while(i<j){
            if (s[i++] != s[j--])
                return false;
        }
        return true;
    }
};