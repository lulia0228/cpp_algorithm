
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        sort(nums.begin() , nums.end());
        return nums[nums.size()/2];
    }
};

//摩尔投票法
class Solution1 {
public:
    int majorityElement(vector<int>& nums) {
        int count = 0;
        int res = 0;
        for(int i=0 ;i < nums.size();i++){
            if( count == 0 ){
                res = nums[i];
                count = 1;
            }
            else{
                if(nums[i] != res)
                    count--;
                else
                    count++;
            }
        }
        return res;
    }
};


//摩尔投票法
class Solution2 {
public:
    int majorityElement(vector<int>& nums) {
        int count = 0;
        int res = 0;
        for(int i=0 ;i < nums.size();i++){
            if(count == 0 || nums[i] == res){
                res = nums[i];
                count++;
            }
            if(nums[i] != res)
                count--;
        }
        return res;
    }
};

class Solution3{
public:
    //找到数组中出现次数超过一半的数字，不存在输出0    L169
    //思路1：标记出现次数（不一定要用字典标记，用2个变量也是可以的）   //思路2：排序后，若存在，则中位数就是要找的，判断中位数出现的总次数
    int findNumberExceedHalf(vector<int>& nums){
        int value = nums[0] ;
        int flag = 1 ;
        for(int i = 1; i < nums.size() ; i++){
            if(flag > 0){
                if(value == nums[i])
                    flag ++ ;
                else
                    flag -- ;
            }
            else{
                value = nums[i];
                flag = 1 ;
            }
        }
        // 找到了value 判断出现次数
        int count= 0 ;
        for(auto  i : nums){
            if(value == nums[i])
                count ++ ;
        }

        if(count > nums.size()/2)
            return value;
        else
            return 0 ;

    }
};

int main(){
    int a[] = {2,2,1,1,1,2,2};
    vector<int> v1(a,a+ sizeof(a)/ sizeof(int));
    cout << Solution().majorityElement(v1)<<endl;
}