//
// Created by LiHeng on 2020/6/30.
//
#include <iostream>
#include <unordered_map>
using namespace std;
class Solution {
public:
    bool isHappy(int n) {
        unordered_map<int, int> um;
        while((n!=1) && um.find(n)==um.end()){
            um[n]++;
            n = getSquareSum(n);
        }
        return n==1;
    }

    int getSquareSum(int n){
        int res = 0;
        while(n>0){
            int d=n%10;
            n = n/10;
            res += d*d;
        }
        return res;
    }
};

// 这道题目，其实和检测链表是否有环是一个原理，具体的看官方解释
// 一种是利用哈希表检测；一种是快慢指针相遇法检测