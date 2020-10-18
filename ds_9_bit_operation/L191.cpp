
#include <iostream>

using namespace std;
class Solution {
public:
    int hammingWeight(uint32_t n) {
        int count = 0;
        uint32_t base = 1;
        for(int i=0; i<32; ++i){
            if((n&base) != 0)
                count++;
            base <<= 1;
        }
        return count;
    }
};


class Solution1 {
public:
    int hammingWeight(uint32_t n) {
        int count = 0;
        while(n){
            n = n&(n-1);
            count++;
        }
        return count ;
    }
};
