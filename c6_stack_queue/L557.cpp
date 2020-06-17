//
// Created by 李恒 on 2020/1/3.
//

// 557 反转字符串中的单词 III

#include <iostream>
#include <cstring>
#include <stack>
using namespace std;

class Solution {
public:
    string reverseWords(string s) {
        string res_str = "";
        string tem_str = "";
        stack<char> stk1;
        for(int i=0 ; i < s.size(); i++){
            if(s[i] == ' '){
                while(!stk1.empty()){
                    tem_str += stk1.top();
                    stk1.pop();
                }
                res_str += tem_str;
                res_str += ' ';
                tem_str = "";
            }
            else
                stk1.push(s[i]);
        }
        while(!stk1.empty()){ //这里要注意的是最后一次因为字符串结尾没有空格。所有栈里面还有数据
            res_str += stk1.top();
            stk1.pop();
        }
        return res_str;
    }

    // leetcode557 给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
    string reverseWordsIII(string s) {
        stack<char> stack1 ;
        string res = "" ;

        for(int i = 0 ; i < s.size() ;i++){

            if(s[i] != ' ')  //遍历字符串，是单个字符，空字符因此用单引号
                stack1.push(s[i]) ;
            else{
                while(!stack1.empty()){
                    res += stack1.top();
                    stack1.pop() ;
                }
                res += " ";
            }
        }

        //最后一次栈中数据还未处理
        while (!stack1.empty()){
            res += stack1.top() ;
            stack1.pop() ;
        }
        return res ;
    }
};


int main(){
    return 0;
}
