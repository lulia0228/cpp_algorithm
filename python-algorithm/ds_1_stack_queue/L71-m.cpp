//
// Created by 李恒 on 2020/7/2.
//
#include <iostream>
#include <stack>
#include <cstring>

using namespace std;

class Solution {
public:
    string simplifyPath(string path) {
        stack<string> stk;
        string res = "";
        string tem = "";
        if(path[path.size()-1] !='/')
            path += '/';

        for(int i=0;i<path.size();i++){
            if(path[i] != '/'){
                tem += path[i];
            }
            else{
                if(tem != ""){
                    if(tem == "."){}
                    else if(tem == ".."){
                        if(!stk.empty())
                            stk.pop();
                    }
                    else
                        stk.push(tem);
                }
                tem = "";
            }
        }
        if(stk.empty())
            return "/";
        while(!stk.empty()){
            res = '/' + stk.top() + res;
            stk.pop();
        }
        return res;
    }
};