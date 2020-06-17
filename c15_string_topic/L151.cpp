//
// Created by liheng on 19-8-28.
//



#include<iostream>
#include<string>
#include<sstream>
#include <vector>
#include <stack>

using namespace std;

class Solution {
public:
    // leetcode 151 给定一个字符串，逐个翻转字符串中的每个单词。
    string reverseWords(string s) {
        vector<string> v_c ;
        string word , res;
        stringstream ss(s);
        while(ss >> word)
            v_c.push_back(word);
        for(int i = v_c.size()-1; i >= 0 ; i-- ){
            if(i == 0)
                res += v_c[i];  //最后不能有空格
            else
                res += v_c[i] + " ";
        }
        return res ;
    }


};

int test151() {
    string str=" abc def ghi ";
    string re = Solution().reverseWords(str);
    cout << re << endl ;
}


int main(){
    test151() ;
    return 0 ;
}

