

// 43 字符串相乘；利用竖式计算；不能直接用两个数字相乘，因为会溢出

#include <iostream>
#include <cstring>
using namespace std;

class Solution {
public:
    string multiply(string num1, string num2) {
        int n1 = num1.size();
        int n2 = num2.size();
        string res = string(n1+n2,'0');
        for(int i=n2-1; i>=0; i--){
            for(int j=n1-1;  j>=0; j--){ //最巧妙的地方就是这个循环体中的内容
                int tem = (res[i+j+1]-'0')+(num1[j]-'0')*(num2[i]-'0');
                res[i+j+1] = tem%10+'0';  //当前位
                res[i+j] += tem/10;       //前一位，res[i+j]已经初始化为'0'，加上int类型自动转化为char，所以此处不加'0'
            }
        }
        //去除首位'0'；截断前面的所有0
        for(int i=0;i<n1+n2;i++){
            if(res[i] != '0')
                return res.substr(i);
        }
        return "0";
    }
};

int main(){
    string s1 = "123456789";
    string s2 = "987654321";
    string res = Solution().multiply(s1,s2);
    cout << res <<endl ;
    return 0;
}