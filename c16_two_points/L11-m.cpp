//
// Created by LiHeng on 2020/4/21.
//
//11 盛最多水的容器

#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    int maxArea(vector<int>& height) {
        int res = 0;
        int left = 0, right = height.size()-1;
        while(left<right){
            res = max(res , min(height[left],height[right])*(right-left));
            if(height[left]<height[right])
                ++left;
            else
                --right;
        }
        return res;
    }
};


int main(){
    int a[] = {1,8,6,2,5,4,8,3,7};
    vector<int> v1(a,a+9);
    cout << Solution().maxArea(v1)<<endl;
}
