

//最接近的三数之和

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int sz = nums.size();
        int m = sz-3 , n = sz-2 , k = sz-1 ;
        sort(nums.begin(), nums.end());
        int res = abs(nums[sz-1] + nums[sz-2] + nums[sz-3] - target);
        for(int i=0; i<nums.size()-2; i++){
            //if(i>0 && nums[i]==nums[i-1])  continue; 可要可不要
            int l = i+1;
            int r = nums.size()-1;
            int flag = 0;
            while(l < r){
                int sum = nums[i] + nums[l] + nums[r];
                //cout << sum << endl;
                if(sum > target){
                    r--;
                    if (abs(nums[i] + nums[l] + nums[r+1]-target) < res){
                        res = abs(nums[i] + nums[1] + nums[r+1]-target);
                        m = i ;
                        n = l ;
                        k = r+1 ;
                    }
                }
                else if (sum == target){ return sum ;}
                else if (sum < target){
                    l++;
                    if (abs(nums[i] + nums[l-1] + nums[r]-target) < res){
                        res = abs(nums[i] + nums[l-1] + nums[r]-target);
                        m = i ;
                        n = l-1 ;
                        k = r ;
                    }
                }
            }
        }
        return nums[m]+nums[n]+nums[k];
    }
};


//别人的思路
class Solution1 {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int minValue = INT_MAX;
        int sum = 0;
        for(int k = 0; k < nums.size()-2; k++){
            if(k>0 && nums[k] == nums[k-1]) continue;
            int i = k+1, j = nums.size()-1;
            while(i<j){
                int s = nums[k] + nums[i] + nums[j] - target;
                if(abs(s) < minValue){
                    minValue = abs(s);
                    sum = nums[k] + nums[i] + nums[j];
                }
                int mid = nums[i];
                int max = nums[j];
                if(s == 0){
                    return sum;
                }
                else if(s < 0){
                    i++;
                    while(nums[i] == mid && i < j) i++;
                }
                else{
                    j--;
                    while(nums[j] == max && j > i) j--;
                }
            }
        }
        return sum;
    }
};


int main(){
//    int a[] = {-1,2,1,-4};
//    int a[] = {1,1,1,0};
//    int a[] = {1,1,-1,-1,3};
    int a[] = {1,2,5,10,11};
    int tar = 12;
    vector<int> v1(a , a+5);
    cout << Solution().threeSumClosest(v1,tar)<<endl;
    return  0;
}
