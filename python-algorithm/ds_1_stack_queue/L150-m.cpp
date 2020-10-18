
#include <iostream>
#include <stack>
#include <vector>
#include <sstream>

//<sstream>库定义了三种类：istringstream、ostringstream和stringstream，分别用来进行流的输入、输出和输入输出操作。

using namespace std;
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> stk;
        for(int i = 0 ;i < tokens.size(); i++){
            if(tokens[i] == "+"){
                int a = stk.top();
                stk.pop();
                int b = stk.top();
                stk.pop();
                stk.push(b+a);
            }
            else if(tokens[i] == "-"){
                int a = stk.top();
                stk.pop();
                int b = stk.top();
                stk.pop();
                stk.push(b-a);
            }
            else if(tokens[i] == "*"){
                int a = stk.top();
                stk.pop();
                int b = stk.top();
                stk.pop();
                stk.push(b*a);
            }
            else if(tokens[i] == "/"){
                int a = stk.top();
                stk.pop();
                int b = stk.top();
                stk.pop();
                stk.push(b/a);
            }
            else
                stk.push(string2Int(tokens[i]));
        }
        return stk.top();
    }

    //数字字符串转数字
    int string2Int(string x ){
        int a  ;
        stringstream ss(x);
        ss >> a;
        return a;
    }
};