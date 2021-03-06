

//动态规划+二叉搜索树
//给定一个有序序列 1 ... n，为了根据序列构建一棵二叉搜索树。我们可以遍历每个数字 i，将该数字作为树根，
//1 ... (i-1) 序列将成为左子树，(i+1) ... n 序列将成为右子树。于是，我们可以递归地从子序列构建子树。
//在上述方法中，由于根各自不同，每棵二叉树都保证是独特的

//问题是计算不同二叉搜索树的个数。为此，我们可以定义两个函数：
//G(n): 长度为n的序列的不同二叉搜索树个数。
//F(i, n): 以i为根的不同二叉搜索树个数(1≤i≤n)

//例如： 序列1,...,7
// F(n)表示以n作为根节点的二叉搜索树的种类 G(n)表示表示以1~n个数可组成的二叉搜索树的种类
// F(3) = G(2) * G(4)    G(2)是元素1,2可构成的左子树的种类，G(4)是元素4,5,6,7可构成的右子树的种类
// G(n) = F(1)+...+F(n)
// 2个公式结合 就得到G(n)的递推公式

//边界条件G(0)=1 G(1)=1 G(0)代表空因此是1种 G(1)代表一个数字因此也是1种

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int numTrees(int n) {
        vector<int> g(n+1, 0);
        g[0] = 1;
        g[1] = 1;
        for(int i=2; i<=n; ++i){
            for(int j=1; j<=i; ++j)
                g[i] += g[j-1]*g[i-j];
        }
        return g[n];
    }
};