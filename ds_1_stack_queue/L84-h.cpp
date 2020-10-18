

// 这道题设计的精巧，比较难；需要在原来的高度数组两两边各添加一个0，用来确定每个出栈元素的左右边界范围
// 每次出栈计算一次面积；每次栈的单调递增性被破坏的时候开始出栈，一直出栈到单调性恢复为止.
// 这个题不太好理解，可以一步步看下过程。


#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int largestRectangleArea(vector<int>& heights){
        int ans = 0;
        vector<int> st;
        heights.insert(heights.begin(), 0);
        heights.push_back(0);
        for (int i = 0; i < heights.size(); i++)
        {
            while (!st.empty() && heights[st.back()] > heights[i])
            {
                int cur = st.back();
                st.pop_back();
                int left = st.back()+1 ; //左边界的计算一定要这样
                int right = i - 1;
                ans = max(ans, (right - left + 1) * heights[cur]);
            }
            st.push_back(i);
        }
        return ans;
    }

};

#include <stack>
class Solution1 {
public:
    int largestRectangleArea(vector<int>& heights){
        int ans = 0;
        stack<int> stk;
        heights.insert(heights.begin(), 0);
        heights.push_back(0);
        for (int i = 0; i < heights.size(); i++)
        {
            while (!stk.empty() && heights[stk.top()] > heights[i])
            {
                int cur = stk.top();
                stk.pop();
                int left = stk.top()+1 ; //左边界的计算一定要这样
                int right = i - 1;
                ans = max(ans, (right - left + 1) * heights[cur]);
            }
            stk.push(i);
        }
        return ans;
    }

};

int main(){
    vector<int> vec{2,1,5,6,2,3};
    cout << Solution().largestRectangleArea(vec)<<endl;
    cout << Solution1().largestRectangleArea(vec)<<endl;
}