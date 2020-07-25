//
// Created by LiHeng on 2020/4/21.
//

//下一个排列

//思路：
//从最末位寻找第一个破坏升序的数nums[pos - 1], 然后在遍历过的数里寻找比该数大的最小的一个数。
//如遍历过的数为[7,6,4,3], nums[pos - 1]为5, 则5需要与6进行交换, 在将[7,5,4,3]改为升序(这里使用reverse)。
//
//遍历过的数从后往前一定是升序, 故改为从前往后升序只需要反转该部分即可。
//寻找第一个比nums[pos - 1]大的数, 只需改为从前往后升序之后, 从升序的第一个数开始遍历比较大小即可。
//

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int pos = nums.size() - 1;
        while (pos > 0 && nums[pos] <= nums[pos - 1])
            pos--;
        reverse(nums.begin() + pos, nums.end());  //逆序
        if (pos > 0){
            int start = pos;
            for (; start < nums.size(); start++){ //寻找第一个大于nums[pos - 1]的数
                if (nums[start] > nums[pos - 1]){
                    swap(nums[start], nums[pos - 1]); //交换
                    break;
                }
            }
        }
    }
};

int main(){
    int a[5] = {1,2,4,3};
    vector<int> vec(a,a+4);
    Solution().nextPermutation(vec);
    for(int i=0 ; i<vec.size(); i++)
            cout << vec[i]<<endl;
}


// 1 从后向前找到第一个破坏升序的数字；
// 2 将该数字之后的序列反转；
// 3 将该数字和反转的序列中比它大且最接近它的数字 交换位置
// 1 2 3 4
// 1 2 4 3
// 1 3 2 4
// 1 3 4 2
// 1 4 2 3
// 1 4 3 2

// 2 1 3 4  第一个破坏升序的数字是3
// 2 1 4 3
// 2 3 1 4
// 2 3 4 1
// 2 4 1 3
// 2 4 3 1

// 3 1 2 4
// 3 1 4 2
// 3 2 1 4
// 3 2 4 1
// 3 4 1 2
// 3 4 2 1

//....
