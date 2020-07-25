//
// Created by 李恒 on 2020/6/29.
//
#include <iostream>

using namespace std;
class Solution {
public:
    int getSum(int a, int b) {
        while(b){
            auto carry = ((unsigned int)(a&b))<<1;
            a = a^b;
            b = carry;
        }
        return a;
    }
};

// a ^ b可以得到两数相加不进位的加法结果
// (a & b) << 1可以得到两数相加产生的进位
//当a & b的结果是负数时，左移就会造成符号位的溢出，所以此处需要转换为unsigned int来避免可能出现的左移越界行为。