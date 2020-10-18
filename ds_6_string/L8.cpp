
//8 字符串转整数
//别人写的很巧妙，好好学学

#include <iostream>
#include <cstring>
using namespace std;
class Solution {
public:
    int myAtoi(string str) {
        int res = 0;
        int i = 0;
        int flag = 1;
        // 1. 检查空格
        while (str[i] == ' ') { i++; }
        // 2. 检查符号
        if (str[i] == '-') { flag = -1; }
        if (str[i] == '+' || str[i] == '-') { i++; }
        // 3. 计算数字
        while (i < str.size() && isdigit(str[i])) {//相当于只要找到一个"+"或者"-"之后只要其之后的不是数字，这个循环就不会执行了
            int r = str[i] - '0';
            // ------ 4. 处理溢出，这是关键步骤 ------
            if (res > INT_MAX / 10 || (res == INT_MAX / 10 && r > 7)) {
                return flag > 0 ? INT_MAX : INT_MIN;
            }
            // ------------------------------------
            res = res * 10 + r;
            i++;
        }
        return flag > 0 ? res : -res;
    }
};


int main(){
    string str1 = "3.1415";
    string str2 = "+-3000";
    string str3 = "-3103";
    cout << Solution().myAtoi(str1)<<endl;
    cout << Solution().myAtoi(str2)<<endl;
    cout << Solution().myAtoi(str3)<<endl;
    return 0;
}