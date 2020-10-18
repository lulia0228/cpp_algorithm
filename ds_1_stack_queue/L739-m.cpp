

#include <iostream>
#include <cstring>
#include <vector>
#include <stack>
using namespace std ;

//方法1  超时 o(n*n)
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& T) {
        int sz = T.size();
        if(sz == 0)
            return vector<int> {0};
        vector<int> res(sz, 0);
        for(int i=0; i<sz-1; ++i){
            int j=i+1;
            while( j<sz && T[j] <= T[i] )
                j++;
            if(j >= sz)
                res[i] = 0;
            else
                res[i] = j-i;
        }
        return res;
    }
};

//方法2 单调栈实现 原题可以转化为求数组中每个元素右边第一个比它大的元素和它本身的距离

//思路：遍历整个数组，如果栈不空，且当前数字大于栈顶元素，那么如果直接入栈的话就不是 递减栈 ，所以需要取出栈顶元素，
//由于当前数字大于栈顶元素的数字，而且一定是第一个大于栈顶元素的数，直接求出下标差就是二者的距离。

// 构造单调递减栈，相当于每次找到一个破坏单调递减的元素时候，对前面的没破坏单调性的元素按顺序算距离，
// 每算完一个，将其从栈顶推出，直到加上该元素重新恢复单调递减，并将该元素推进栈

class Solution1 {
public:
    vector<int> dailyTemperatures(vector<int>& T) {
        int sz = T.size();
        if (sz == 0)
            return vector<int> ();
        vector<int> res(sz, 0);
        stack<int> stk; //存储下标
        for(int i=0; i<sz; i++){
            if(stk.empty() || T[i]<=T[stk.top()])
                stk.push(i);
            else{
                while( !stk.empty() && T[i]>T[stk.top()] ){
                    res[stk.top()] = i-stk.top();
                    stk.pop();
                }
                stk.push(i);
            }
        }
        return res;
    }
};


//相关题目推荐
//利用堆栈，还可以解决如下常见问题：
//求解算术表达式的结果（LeetCode 224、227、772、770)
//求解直方图里最大的矩形区域（LeetCode 84）

//单调栈适合的问题
//计算数组中每个数右边（或左边）第一个比它大（或小）的数，并计算二者之间的距离。
//寻找数组中的某个子数组，使得子数组中的最小值乘以子数组的长度最大。
//寻找数组中的某个子数组，使得子数组中最小值乘以子数组所有元素和最大。

