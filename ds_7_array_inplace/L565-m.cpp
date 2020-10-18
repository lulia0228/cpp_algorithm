
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int arrayNesting(vector<int>& nums) {
        int res = 0;
        for(int i=0; i< nums.size(); ++i){
            int tmp_len = 0,index = i;
            //当前等于-1说明之前的元素已经访问过当前位置了
            while(nums[index] != -1){
                ++tmp_len;
                int tmp = nums[index];
                cout << nums[index]<<endl;
                nums[index] = -1; // 标记该位置已经被访问
                index = tmp;
            }
            cout << "**************" << endl;
            res = max(res, tmp_len);
        }
        return res;
    }

};

//超时，上面的做法则是做了剪枝
class Solution1 {
public:
    int arrayNesting(vector<int>& nums) {
        int res = 0;
        for(int i=0; i< nums.size(); ++i){
            int tmp_len = 0,index = i;
            do{
                ++tmp_len;
                cout << nums[index]<<endl;
                index = nums[index];
            }while(index != i);
            cout << "**************" << endl;
            res = max(res, tmp_len);
        }
        return res;
    }

};

int main(){
    vector<int> v1 = {5,4,0,3,1,6,2};
    int res = Solution().arrayNesting(v1);
    //cout << res << endl;
}