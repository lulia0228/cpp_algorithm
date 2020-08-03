//
// Created by 李恒 on 2020/1/3.
//

//栈的问题，要注意栈为空的边界处理

//  20 有效的括号
#include <iostream>
#include <cstring>
#include <stack>

using  namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> stk1;
        for(int i=0 ;i<s.size();i++){
            if(s[i]=='('||s[i]=='['||s[i]=='{')
                stk1.push(s[i]);
            else{
                char tem_char ;
                if(s[i] == ')')
                    tem_char = '(';
                else if(s[i] == ']')
                    tem_char = '[';
                else
                    tem_char = '{';
                if(stk1.empty() || stk1.top() != tem_char) //注意一定要判定栈为空(为空代表没有匹配值)；此外栈为空时候取栈顶元素会报错
                    return false;
                stk1.pop();
            }
        }
        if(!stk1.empty()) //意味着栈中还有值，字符串不合法
            return false;
        return true;
    }
};

//使用栈要注意栈是否为空以及栈中最后是否有值。
int main(){
    string str1("[{()}]");
    cout << Solution().isValid(str1)<<endl;
}