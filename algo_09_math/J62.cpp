//
// Created by LiHeng on 2020/7/1.
//
#include <iostream>
using  namespace std;
class Solution {
public:
    int lastRemaining(int n, int m) {
        int p=0;
        for(int i = 2; i <= n; i++){
            p = (p+m)%i;
        }
        return p;
    }
};

//递推公式f(n,m) = [f(n-1,m)+m]%n