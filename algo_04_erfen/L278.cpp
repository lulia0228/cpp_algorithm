

#include <iostream>

using namespace std ;
// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int lt=1, rt=n, mid;
        while(lt < rt){
            mid = lt +(rt-lt)/2;
            if(isBadVersion(mid))
                rt = mid;
            else
                lt = mid+1;
        }
        return rt;
    }
};