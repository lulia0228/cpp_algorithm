

// 数组只能读 所以不能排序,不能swap数组下标
// 时间复杂度小于 O(n^2) 不能暴力
// 空间复杂度 O(1) 不能额外开辟数组

#include <iostream>
#include <vector>

using namespace std;

//方法1 循环检测的方法  抽象成环链表寻找入口位置的问题 应该是o(n)
/*
 * 将这个题目给的特殊的数组当作一个链表来看，数组的下标就是指向元素的指针，把数组的元素也看作指针。
 * 如0是指针，指向nums[0]，而nums[0]也是指针，指向nums[nums[0]].

int point = 0;
while(true){
point = nums[point]; // 等同于 next = next->next;
}
*/

class Solution1 {
public:
    int findDuplicate(vector<int>& nums) {
        int result = 0;
        int slow = nums[0];
        int quick = nums[0];
        do{
            slow = nums[slow]; //把元素值当做指针（下一个元素的索引）
            quick = nums[nums[quick]]; //相当于两次quick = nums[quick]
        }while(slow!=quick);

        int p = nums[0];
        while(p!=quick){
            p = nums[p];
            quick = nums[quick];
        }

        return p;
    }
};

class Solution2 {
public:
    int findDuplicate(vector<int>& nums) {

        int fast = 0, slow = 0;
        while(true){
            fast = nums[nums[fast]]; //相当于走两步:等效执行两次fast=nums[fast]
            slow = nums[slow]; //相当于走一步；这个操作太神奇了
            if(fast == slow)
                break;
        }

        //先相遇，再分别从起始和相遇点往前走，再相遇必然是入口
        int finder = 0;
        while(true){
            finder = nums[finder];
            slow = nums[slow];
            if(slow == finder)
                break;
        }
        return finder;
    }
};


//方法2 二分法+遍历 O(nlogn) 抽屉原理 也没去深究
class Solution {
public:
    int findDuplicate(vector<int> &nums) {
        int len = nums.size();
        int left = 1;
        int right = len - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            int cnt = 0;
            for (int num:nums) {
                if (num <= mid) {
                    cnt++;
                }
            }
            // 根据抽屉原理，小于等于 4 的数的个数如果严格大于 4 个，
            // 此时重复元素一定出现在 [1, 4] 区间里

            if (cnt > mid) {
                // 重复的元素一定出现在 [left, mid] 区间里
                right = mid;
            } else {
                // if 分析正确了以后，else 搜索的区间就是 if 的反面
                // [mid + 1, right]
                // 注意：此时需要调整中位数的取法为上取整
                left = mid + 1;
            }
        }
        return left;
    }
};

