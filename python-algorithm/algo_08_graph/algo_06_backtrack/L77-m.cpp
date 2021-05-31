

//带循环的递归，注意皇后问题51和全排列46、组合77这3道题目问题对比
//组合问题 leetcode 77 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合


#include <iostream>
#include <cassert>
#include <vector>

using namespace std;
class Solution{
private:
    vector<vector<int>> res ;
    //求解c(n,k) 当前已经找到的组合存储在c中，从start位置寻找新的元素
    void generateCombinatons(int n , int k , int start , vector<int> &c){
        //递归终止条件
        if(c.size() == k){
            res.push_back(c);
            return;
        }
        // 这里有优化的空间（剪枝），每次遍历 i 不必都要走到n ; 当前情况下c中还差的元素个数为 k - c.size();
        // 因此[i=start ,..., n]中至少要有 k - c.size()个元素，因此当前i=start最大是 n -(k - c.size()) + 1
        // 即for(int i = start ; i <= n -(k - c.size()) + 1 ; i ++)
        for(int i = start ; i <= n ; i ++){
            c.push_back(i) ;
            generateCombinatons(n , k , i + 1 , c);
            c.pop_back();
        }
        return;
    }

public:
    vector<vector<int>> combine(int n , int k){
        res.clear() ;
        if(n <= 0 || k <= 0 || k > n)
            return  res ;
        vector<int> c ;
        generateCombinatons(n , k , 1 ,c );
        return res ;
    }
};

int main(){
    int n = 4 , k = 2 ;
    vector<vector<int>> re = Solution().combine(n , k );
    for(int i = 0 ; i < re.size() ; i++ ){
        for(int j = 0 ; j < re[i].size() ; j++)
            cout << re[i][j] << "\t" ;
        cout << endl ;
    }
}

//练习leetcode 39 40 216 78 90 401