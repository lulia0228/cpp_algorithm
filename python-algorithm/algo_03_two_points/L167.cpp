

//已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

#include <iostream>
#include <vector>
using namespace std;

class  Solution{
public:
    //leetcode two sum 167
    vector<int> twoSum(vector<int>& numbers, int target) {
        int i =  0 , j = numbers.size()-1 ;
        vector<int> res ;
        while(i < j){
            int sum = numbers[i] + numbers[j] ;
            if(sum == target){
                res.push_back(i+1);
                res.push_back(j+1);
                return res ; //这句话一定不能漏掉，提前终止。不然会继续循环下去
            }
            else if (sum > target)
                j--;
            else
                i++ ;
        }
        return res ;
    }
};


int main(){
    int arr[5] = {1,2,4,6,7};
    vector<int> vec (arr, arr+5);
    vector<int>  s_list = Solution().twoSum(vec, 8);
    for(int i = 0 ; i< s_list.size(); i++)
        cout<< s_list[i]<< " ";
}

// 以上做法有多种解得时候 只能返回其中一种

