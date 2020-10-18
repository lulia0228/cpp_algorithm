

//爬楼梯

#include <iostream>
using namespace std;

class Solution {
public:
    int climbStairs(int n) {
        if(n<3)
            return n;
        int a = 1;
        int b = 2;
        int c ;
        for(int i=3 ; i<=n ; i++){
            c = a + b;
            a = b;
            b = c;
        }
        return c;
    }
};

int main(){
    return  0;
}