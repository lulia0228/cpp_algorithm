

#include <iostream>
#include <cassert>
#include <vector>

using namespace std ;

class Solution{
public:
    //leetcode 70 爬楼梯
    int climbStairs(int n) {
        if(n == 0 || n == 1 || n == 2)
            return n ;
        int a[n+1] ;
        a[1] = 1 ;
        a[2] = 2 ;
        for(int i = 3 ; i <= n ; i++){
            a[i] = a[i-1] + a[i-2];
        }
        return a[n] ;
    }

    //变态跳台阶 f(n)=2f(n-1)
    int climbStairsB(int n) {
        if(n == 0 || n == 1 || n == 2)
            return n ;
        int a[n+1] ;
        a[1] = 1 ;
        a[2] = 2 ;
        for(int i = 3 ; i <= n ; i++){
            a[i] = 2* a[i-1];
        }
        return a[n] ;
    }

    //斐波那契数列
    int Fib(int n){
        assert(n >= 1) ;
        if(n == 1 || n == 2)
            return 1 ;
        int a = 1 , b = 1 , c = 0 ;
        for(int i = 3 ; i <= n ; i++){
            int c = a + b ;
            b = a ;
            a = c ;
        }
        return c ;

    }

    //leetcode 704 二分查找
    int search(vector<int>& nums, int target) {
        int i = 0;
        int j = nums.size() -1 ;
        while(i <= j){
            int middle = i + (j - i)/2 ;
            if(nums[middle] == target)
                return middle ;
            else if (nums[middle] > target)
                j = middle - 1 ;
            else
                i = middle + 1 ;
        }
        return -1 ;
    }

    //剑指offer 1
    bool findt(int target, vector<vector<int> > array) {
        if(array.size() == 0 || array[0].size() == 0)
            return false ;
        int row = 0;
        int col = array[0].size()-1;
        while(row < array.size() && col >= 0){
            if(array[row][col] == target)
                return true;
            else if(array[row][col] > target)
                col -- ;
            else
                row ++ ;
        }
        return false ;
    }
    
};

int main(){
    vector<vector<int>> vec(10 ,vector<int>(8)) ;
    for(int i = 0 ; i < 10 ; i++){
        for(int j = 0 ;j < 8 ; j++){
            vec[i][j] = i*10 + j;
        }
    }
    cout << Solution().findt(67 , vec) ;
}

/*
#include <stack>
//用两个栈实现队列（剑指Offer）
class stack2queue{
    stack<int> stack1 ;
    stack<int> stack2 ;
public:
    void push(int node){
        stack1.push(node) ;
    }

    int pop(){
        if(stack1.empty() && stack2.empty())
            throw runtime_error("Queue is empty!") ;
        if(stack2.empty()){
            while(!stack1.empty()){
                stack2.push(stack1.top());
                stack1.pop() ;
            }
        }
        int re = stack2.top() ;
        stack2.pop() ;
        return re ;
    }
};
*/
