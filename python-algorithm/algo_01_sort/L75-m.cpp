//
// Created by LiHeng on 2020/4/22.
//

//三色分类
#include <iostream>
#include <vector>
using namespace std;


//最快
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int i=0, j=nums.size()-1;
        //必须是k<=j ，j是变化的，否则后面的2 又被交换到前面去了
        for(int k=0; k<=j; k++){
            if (nums[k] == 0){
                swap(nums[i],nums[k]);
                i++; //0换到前面后当前元素值一定≥0
            }
            // 对当前元素而言先把0换到最前面；换完后如果是2就把2换到最后面
            else if (nums[k] == 2){ //这里用if  和else if 都可以AC
                swap(nums[k],nums[j]);
                j--;
                k--; //最关键的地方。开始没有加这行就是错的；为了保证所有2都到后面必须加这行即换完了之后再检查
            }
        }
        return;
    }
};


class Solution1{
public:
    void sortColors(vector<int> & nums){
        int count[3] = {0} ; //存放元素频率

        for (int i = 0 ; i < nums.size(); i ++){
            assert(nums[i] >= 0 && nums[i] <= 3);
            count[nums[i]]++;
        }

        int index = 0;
        for (int i = 0; i < 3; i++){
            for (int j = 0 ; j < count[i]; j++)
                nums[index++] = i;
        }
    }
};



//三路快排的思路
class Solution2{
public:
    void sortColors(vector<int> & nums){
        int zero = -1;
        int two = nums.size(); //用2个索引分成3块

        for (int i = 0 ; i < two; ){
            if (nums[i] == 1)
                i++;
            else if (nums[i] == 2)
                swap(nums[i], nums[--two]);
            else // 即nums[i]==0
                swap(nums[i++], nums[++zero]);
        }
    }
};


int main(){
    int arr[] = {0,1,0,2,1,2,1,2,1,0,0,0,0,2,2,1,0,2,1,2};
    vector<int> vec(arr, arr + sizeof(arr)/ sizeof(int));
    Solution().sortColors(vec);
    for (int i = 0 ; i < vec.size(); i++)
        cout<< vec[i]<<" ";
}

//练习:leetcode 88  215