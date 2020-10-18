
#include <iostream>
#include <stack>
#include <cstring>
using  namespace std;
class Solution {
public:
    string decodeString(string s) {
        stack<char> stk;
        for(int i=0 ; i<s.size(); i++){
            if (s[i] == ']'){
                string tem_str;
                while(!stk.empty() && stk.top() != '['){
                    tem_str = stk.top()+tem_str;
                    stk.pop();
                }
                stk.pop(); //弹出'['
                string num_str;
                //注意'0'<=stk.top()<='9'这么写是错的
                while(!stk.empty() && stk.top()<='9' && stk.top()>=0){
                    num_str = stk.top()+num_str;
                    stk.pop();
                }
                int tem_num = str2num(num_str);

                for(int i=0; i<tem_num; i++)
                    for (char c: tem_str)
                        stk.push(c);
            }
            else
                stk.push(s[i]);
        }
        string res;
        while(!stk.empty()){
            res = stk.top()+res;
            stk.pop();
        }
        return res;
    }

    int str2num(string s){
        int res = 0;
        for(int i=0; i<s.size(); ++i)
            res = res*10 + int(s[i]-'0');
        return res;
    }
};

int main(){
    string s = "3[a]2[bc]";
    string res = Solution().decodeString(s);
    cout << res << endl;
}