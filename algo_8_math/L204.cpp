//
// Created by LiHeng on 2020/6/30.
//
#include <iostream>

using namespace std;
class Solution {
public:
    int countPrimes(int n) {
        if(n <= 2)
            return 0;
        int count = 1;
        for(int i=3; i<n; ++i){
            if(i%2 == 0)
                continue;
            if(isP(i))
                count++;
        }
        return count;
    }

    bool isP(int num){
        for(int k=2; k*k<=num; ++k){
            if(num%k == 0)
                return false;
        }
        return true;
    }

};