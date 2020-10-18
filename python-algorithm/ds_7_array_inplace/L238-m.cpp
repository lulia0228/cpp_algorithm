
//除自身以外乘积数组
//要求时间复杂度o(1)，所以想到了空间换时间；还有更高级的做法，空间复杂度也低

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> res ;
        int sz = nums.size();
        vector<int> c(sz,1);
        vector<int> d(sz,1);
        for(int i=1 ;i<sz;i++)
            c[i] = c[i-1]*nums[i-1];
        for(int i=sz-2;i>=0 ;i--)
            d[i] = d[i+1]*nums[i+1];
        for(int i= 0 ;i<sz;i++)
            res.push_back(c[i]*d[i]);
        return res;
    }
};


int main(){
    int a[] = {1,2,3,4};
    vector<int> v1(a,a+4);
    vector<int> re = Solution().productExceptSelf(v1);
    for(vector<int>::iterator it = re.begin(); it != re.end();it++)
        cout << *it << endl;
    return 0;
}

