
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
        int sz = letters.size();
        int lt=0, rt=sz-1,mid;
        if(letters[0] > target || letters[sz-1] <= target)
            return letters[0];
        while(lt < rt){
            mid = lt +(rt-lt)/2;
            if(letters[mid] <= target)
                lt = mid+1;
            else
                rt = mid;
        }
        return letters[lt];
    }
};