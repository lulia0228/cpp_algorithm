# -*- coding: utf-8 -*-


'''给定两个字符串形式的非负整数 num1 和num2 ，计算它们的差。
注意：
num1 和num2 都只会包含数字 0-9
num1 和num2 都不包含任何前导零
你不能使用任何內建 BigInteger 库
'''

'''
#include <iostream>
#include <algorithm>
using namespace std;

string sub(string a, string b) {
    string res = "";
    int borrow = 0;
    int i = a.size() - 1, j = b.size() - 1;
    while (i >= 0 || j >= 0) {
        int x = i >= 0 ? a[i] - '0' : 0;
        int y = j >= 0 ? b[j] - '0' : 0;
        int z = (x - borrow - y + 10) % 10;
        res += '0' + z;
        borrow = x - borrow - y < 0 ? 1 : 0;
        i--, j--;
    }
    reverse(res.begin(), res.end());
    //删除前导0。循环条件是res.size()-1是为防止"0000"的情况
    int pos;
    for (pos = 0; pos < res.size() - 1; pos++) {
        if (res[pos] != '0') break;
    }
    return res.substr(pos);
}

bool cmp(string a, string b) {
    if (a.size() == b.size()) return a < b;
    return a.size() < b.size();
}

string subStrings(string num1, string num2) {
    string res;
    if (cmp(num1, num2)) {
        res = sub(num2, num1);
        if (res != "0") res.insert(0, "-");
    }
    else res = sub(num1, num2);
    return res;
}

int main() {
    string a, b, c;
    cin >> a >> b;
    cout << subStrings(a, b) << endl;
    return 0;
}

'''