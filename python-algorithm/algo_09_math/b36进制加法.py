# -*- coding: utf-8 -*-


'''
36进制由0-9，a-z，共36个字符表示。
要求按照加法规则计算出任意两个36进制正整数的和，如1b + 2x = 48  （解释：47+105=152）
要求：不允许使用先将36进制数字整体转为10进制，相加后再转回为36进制的做法
'''

# 此题难度倒不是很大，实际上是LC415. 字符串相加的扩展。
# LC415是十进制的大数相加，而本题是36进制的大数相加。

'''
string addStrings(string num1, string num2)
{
    int carry = 0;
    int i = num1.size() - 1, j = num2.size() - 1;
    string res;
    while (i >= 0 || j >= 0 || carry)
    {
        int x = i >= 0 ? num1[i] - '0' : 0;
        int y = j >= 0 ? num2[j] - '0' : 0;
        int temp = x + y + carry;
        res += '0' + temp % 10;
        carry = temp / 10;
        i--, j--;
    }
    reverse(res.begin(), res.end());
    return res;
}

#include <iostream>
#include <algorithm>
using namespace std;

char getChar(int n)
{
    if (n <= 9)
        return n + '0';
    else
        return n - 10 + 'a';
}
int getInt(char ch)
{
    if ('0' <= ch && ch <= '9')
        return ch - '0';
    else
        return ch - 'a' + 10;
}
string add36Strings(string num1, string num2)
{
    int carry = 0;
    int i = num1.size() - 1, j = num2.size() - 1;
    int x, y;
    string res;
    while (i >= 0 || j >= 0 || carry)
    {
        x = i >= 0 ? getInt(num1[i]) : 0;
        y = j >= 0 ? getInt(num2[j]) : 0;
        int temp = x + y + carry;
        res += getChar(temp % 36);
        carry = temp / 36;
        i--, j--;
    }
    reverse(res.begin(), res.end());
    return res;
}

int main()
{
    string a = "1b", b = "2x", c;
    c = add36Strings(a, b);
    cout << c << endl;
}

'''