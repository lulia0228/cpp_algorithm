# -*- coding: utf-8 -*-
'''题目描述
36进制由0-9，a-z，共36个字符表示。
要求按照减法规则计算出任意两个36进制正整数的差，如48-2x =1b  （解释：152-105=47）
要求：不允许使用先将36进制数字整体转为10进制，相减后再转回为36进制的做法'''

'''
#include <iostream>
#include <algorithm>
using namespace std;

char getChar(int n) {
    if (n <= 9) return n + '0';
    else return n - 10 + 'a';
}

int getInt(char ch) {
    if ('0' <= ch && ch <= '9') return ch - '0';
    else return ch - 'a' + 10;
}

string sub(string a, string b) {
    string res = "";
    int borrow = 0;
    int i = a.size() - 1, j = b.size() - 1;
    while (i >= 0 || j >= 0) {
        int x = i >= 0 ? getInt(a[i]) : 0;
        int y = j >= 0 ? getInt(b[j]) : 0;
        int z = (x - borrow - y + 36) % 36;
        res += getChar(z);
        borrow = x - borrow - y < 0 ? 1 : 0;
        i--, j--;
    }
    reverse(res.begin(), res.end());
    //删除前导0。注意：循环条件是res.size()-1是为防止"0000"的情况
    int pos;
    for (pos = 0; pos < res.size() - 1; pos++) {
        if (res[pos] != '0') break;
    }
    return res.substr(pos);
}

bool isLess(string a, string b) {
    if (a.size() == b.size()) return a < b;
    return a.size() < b.size();
}

string subStrings(string num1, string num2) {
    string res;
    if (isLess(num1, num2)) {
        res = sub(num2, num1);
        res.insert(0, "-");
    }
    else res = sub(num1, num2);
    return res;
}

int main() {
    string a, b;
    cin >> a >> b;
    cout << subStrings(a, b) << endl;
    return 0;
    
}'''