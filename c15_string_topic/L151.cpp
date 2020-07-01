//
// Created by liheng on 19-8-28.
//

//151 翻转字符串中的每个单词
#include<iostream>
#include<cstring>

using namespace std;

class Solution {
public:
    string reverseWords(string s) {
        int sz = s.size();
        string res = "";
        string tmp = "";
        for(int i=sz-1; i>=0; --i){
            if(s[i] == ' '){
                if(tmp != ""){
                    res += tmp;
                    res += " ";
                }
                tmp = "";
            }
            else
                tmp = s[i]+tmp;
        }
        return tmp == ""?res.substr(0,res.size()-1):res + tmp;
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

