
//数组中的第K个最大元素
#include <iostream>
#include <queue>

using namespace std;


class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int, vector<int>, greater<int> > c; //小顶堆
        for(int i=0 ; i<nums.size(); i++){
            if (c.size()< k)
                c.push(nums[i]);
            else {
                if(nums[i] > c.top()){
                    c.pop();
                    c.push(nums[i]);
                }
            }
        }
        return c.top();
    }
};


int main(){
    return 0;
}