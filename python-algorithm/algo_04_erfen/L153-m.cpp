
#include <iostream>
#include <cassert>
#include <vector>

//我的写法
using namespace std ;
class Solution {
public:
    int findMin(vector<int>& nums) {
        int sz = nums.size();
        if(nums[0] < nums[sz-1])
            return nums[0];
        int lt=0, rt=sz-1, mid;
        while(lt < rt){
            mid = lt + (rt-lt)/2;
            if(nums[mid] >= nums[0]) //这里比较mid与left是行不通的
                lt = mid+1;
            else
                rt = mid;
        }
        return nums[lt];
    }
};


class Solution1 {
public:
    int findMin(vector<int>& nums) {
        int sz = nums.size();
        if(nums[0] < nums[sz-1])
            return nums[0];
        int lt=0, rt=sz-1, mid;
        while(lt < rt){
            mid = lt + (rt-lt)/2;
            //if(nums[mid] < nums[rt]) 也可以通过
            if(nums[mid] <= nums[rt])
                rt = mid;
            else
                lt = mid+1;
        }
        return nums[lt];
    }
};


int main(){
    vector<int> v1 ={2,2,2,0,1};
    int res = Solution().findMin(v1);
    cout << res <<endl;

}