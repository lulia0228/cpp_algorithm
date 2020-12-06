<!-- GFM-TOC -->
* [一、栈和队列](#栈和队列)
    * [1. 用两个栈实现队列](#1-用两个栈实现队列)
    * [2. 包含min函数的栈](#2-包含min函数的栈)
    * [3. 队列的最大值](#3-队列的最大值)   
    * [4. 滑动窗口的最大值](#4-滑动窗口的最大值)   

* [二、滑动窗口](#滑动窗口)
   * [1. 和为s的连续正数序列](#1-和为s的连续正数序列)
   * [2. 最长不含重复字符的子字符串](#2-最长不含重复字符的子字符串)
   
* [三、堆的应用](#堆的应用)
    * [1. 最小的k个数 ](#1-最小的k个数 )
    * [2. 数据流中的中位数](#2-数据流中的中位数)
    
* [四、位运算](#位运算)
    * [1. 二进制中1的个数](#1-二进制中1的个数)
    * [2. 数组中出现次数超过一半的数字](#2-数组中出现次数超过一半的数字)
    
* [五、树相关](#树相关)
    * [1. 二叉树的深度](#1-二叉树的深度)
    * [2. 平衡二叉树](#2-平衡二叉树)
    * [3. 对称的二叉树](#3-对称的二叉树)
    * [4. 二叉树的镜像](#4-二叉树的镜像)
    * [5. 树的子结构](#5-树的子结构)
    * [6. 从上到下打印二叉树](#6-从上到下打印二叉树)
    * [7. 从上到下打印二叉树II](#7-从上到下打印二叉树II)
    * [8. 从上到下打印二叉树III](#8-从上到下打印二叉树III)
    * [9. 重建二叉树](#9-重建二叉树)
    * [10. 序列化二叉树](#10-序列化二叉树)
    * [11. 二叉树中和为某一值的路径](#11-二叉树中和为某一值的路径)
    * [12. 二叉搜索树的第k大节点](#12-二叉搜索树的第k大节点)
    * [13. 二叉搜索树的最近公共祖先  ](#13-二叉搜索树的最近公共祖先  )
    * [14. 二叉树的最近公共祖先](#14-二叉树的最近公共祖先) 

* [六、链表相关](#链表相关)
    * [1. 从尾到头打印链表](#1-从尾到头打印链表)
    * [2. 删除链表的节点](#2-删除链表的节点)
    * [3. 链表中倒数第k个节点](#3-链表中倒数第k个节点)
    * [4. 反转链表](#4-反转链表)
    * [5. 两个链表的第一个公共节点](#5-两个链表的第一个公共节点)
    * [6. 合并两个排序的链表](#6-合并两个排序的链表)
    * [7. 二叉搜索树与双向链表](#7-二叉搜索树与双向链表)
    
* [七、二分查找](#二分查找)
    * [1. 二维数组中的查找](#1-二维数组中的查找)
    * [2. 旋转数组的最小数字](#2-旋转数组的最小数字)
    * [3. 在排序数组中查找数字I](#3-在排序数组中查找数字I)
    * [4. 0到n-1中缺失的数字](#4-0到n-1中缺失的数字)

* [八、动态规划](#动态规划)
    * [1. 剪绳子](#1-剪绳子)
    * [2. 连续子数组的最大和](#2-连续子数组的最大和)
    * [3. 礼物的最大价值](#3-礼物的最大价值)
    * [4. 股票的最大利润](#4-股票的最大利润)   
    * [5. n个骰子的点数](#4-n个骰子的点数)  

   
   
  
* [股票问题](#股票问题)
    * [1. 买卖股票一次交易](#1-买卖股票一次交易)
    * [2. 买卖股票不限次数](#2-买卖股票不限次数)
    * [3. 最佳买卖股票时机含冷冻期不限次数](#3-最佳买卖股票时机含冷冻期不限次数)
    * [4. 买卖股票的最佳时机含手续费不限次数](#4-买卖股票的最佳时机含手续费不限次数)
    * [5. 只能进行两次的股票交易](#5-只能进行两次的股票交易)
    * [6. 只能进行k次的股票交易](#6-只能进行k次的股票交易)

<!-- GFM-TOC -->


# 栈和队列
## 1 用两个栈实现队列   
剑指 Offer 09  

[力扣](https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/) / [Python3](./python-algorithm/sword_point_offer/J09.py)    

## 2 包含min函数的栈
剑指 Offer 30    

```
题目：定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。
```
[力扣](https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof/) / [Python3](./python-algorithm/sword_point_offer/J30.py) 

## 3 队列的最大值    
剑指 Offer 59  

```
题目：请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。
```
[力扣](https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof/) / [Python3](./python-algorithm/sword_point_offer/J59_2.py)    

## 4 滑动窗口的最大值    
剑指 Offer 59 - I. 

```
题目：给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。
输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7] 
```
[力扣](https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/) / [Python3](./python-algorithm/sword_point_offer/J59_1.py)    

# 滑动窗口  
## 1 和为s的连续正数序列
剑指 Offer 57 - II. 

[力扣](https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/) / [Python3](./python-algorithm/sword_point_offer/J57_2.py) 
```
题目:输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

示例 1：
输入：target = 9
输出：[[2,3,4],[4,5]]

示例 2：
输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]
```

## 2 最长不含重复字符的子字符串
剑指 Offer 48. 

[力扣](https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/) / [Python3](./python-algorithm/sword_point_offer/J48.py) 
```
题目:请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。
示例 1:
输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
```


# 堆的应用   
## 1 最小的k个数  
剑指 Offer 40   

[力扣](https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/) / [Python3](./python-algorithm/sword_point_offer/J40.py)     
```
题目: 输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。
```

## 2 数据流中的中位数  
剑指 Offer 41  

[力扣](https://leetcode-cn.com/problems/shu-ju-liu-zhong-de-zhong-wei-shu-lcof/) / [Python3](./python-algorithm/sword_point_offer/J41-h.py)    
```
题目：如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
例如，[2,3,4] 的中位数是 3
[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：
void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。
```


# 位运算
## 1 二进制中1的个数
剑指 Offer 15         

[力扣](https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/) / [Python3](./python-algorithm/sword_point_offer/J15.py)      
```
题目: 输入一个整数（以二进制串形式），输出该数二进制表示中 1 的个数。
```

## 2 数组中出现次数超过一半的数字
剑指 Offer 39      

[力扣](https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/) / [Python3](./python-algorithm/sword_point_offer/J39.py)      
```
题目:数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。
```


# 树相关
## 1 二叉树的深度  
剑指 Offer 55 - I.   

[力扣](https://leetcode-cn.com/problems/er-cha-shu-de-shen-du-lcof/) / [Python3](./python-algorithm/sword_point_offer/J39.py)      

## 2 平衡二叉树
剑指 Offer 55 - II. 

[力扣](https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof/) / [Python3](./python-algorithm/sword_point_offer/J39.py)      
```
题目:给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
```

## 3 对称的二叉树
剑指 Offer 28.    

[力扣](https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof/) / [Python3](./python-algorithm/sword_point_offer/J28.py)      
```
题目:请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。
例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
```

## 4 二叉树的镜像
剑指 Offer 27.   

[力扣](https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof/) / [Python3](./python-algorithm/sword_point_offer/J27.py)      
```
题目：请完成一个函数，输入一个二叉树，该函数输出它的镜像。
例如输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
镜像输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1

```

## 5 树的子结构
剑指 Offer 26. 

[力扣](https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof/) / [Python3](./python-algorithm/sword_point_offer/J26-m.py)      
```
题目:输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)
B是A的子结构， 即 A中有出现和B相同的结构和节点值。
例如:
给定的树 A:

     3
    / \
   4   5
  / \
 1   2
给定的树 B：

   4 
  /
 1
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。
```

## 6 从上到下打印二叉树
剑指 Offer 32 - I

[力扣](https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof/) / [Python3](./python-algorithm/sword_point_offer/J32_1.py)      
```
题目: 例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回：

[3,9,20,15,7]
```

## 7 从上到下打印二叉树II
剑指 Offer 32 - II

[力扣](https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof/) / [Python3](./python-algorithm/sword_point_offer/J32_2.py)      
```
题目: 例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
```

## 8 从上到下打印二叉树III
剑指 Offer 32 - III

[力扣](https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/) / [Python3](./python-algorithm/sword_point_offer/J32_3.py)      
```
题目:例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [20,9],
  [15,7]
]
```

## 9 重建二叉树
剑指 Offer 07. 

[力扣](https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof/) / [Python3](./python-algorithm/sword_point_offer/J07-m.py)      
```
题目:输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如，给出
   前序遍历 preorder = [3,9,20,15,7]
   中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：
                3
               / \
              9  20
                /  \
               15   7
```

## 10 序列化二叉树
剑指 Offer 37.    

[力扣](https://leetcode-cn.com/problems/xu-lie-hua-er-cha-shu-lcof/) / [Python3](./python-algorithm/sword_point_offer/J37-h.py)      
```
题目: 请实现两个函数，分别用来序列化和反序列化二叉树。
示例: 
你可以将以下二叉树：
          1
         / \
        2   3
           / \
          4   5
序列化为 "[1,2,3,null,null,4,5]"
```

## 11 二叉树中和为某一值的路径
剑指 Offer 34. 

[力扣](https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/) / [Python3](./python-algorithm/sword_point_offer/J34-m.py)      
```
示例:给定如下二叉树，以及目标和 sum = 22，
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:
         [
            [5,4,11,2],
            [5,8,4,5]
         ]
```

## 12 二叉搜索树的第k大节点
剑指 Offer 54. 

[力扣](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/) / [Python3](./python-algorithm/sword_point_offer/J54.py)      
```
题目:给定一棵二叉搜索树，请找出其中第k大的节点。
```

## 13 二叉搜索树的最近公共祖先
剑指 Offer 68 - I.   

[力扣](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof/) / [Python3](./python-algorithm/sword_point_offer/J68_1-m.py)      


## 14 二叉树的最近公共祖先
剑指 Offer 68 - II.  

[力扣](https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof/) / [Python3](./python-algorithm/sword_point_offer/J68_2-m.py)       



# 链表相关
## 1 从尾到头打印链表   
剑指 Offer 06. 

[力扣](https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/) / [Python3](./python-algorithm/sword_point_offer/J06.py) 

## 2 删除链表的节点
剑指 Offer 18.   

[力扣](https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof/) / [Python3](./python-algorithm/sword_point_offer/J18.py) 

## 3 链表中倒数第k个节点 
剑指 Offer 22. 
   
[力扣](https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/) / [Python3](./python-algorithm/sword_point_offer/J22.py) 

## 4 反转链表
剑指 Offer 24. 

[力扣](https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/) / [Python3](./python-algorithm/sword_point_offer/J24.py) 

## 5 两个链表的第一个公共节点  
剑指 Offer 52. 

[力扣](https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/) / [Python3](./python-algorithm/sword_point_offer/J52.py) 

## 6 合并两个排序的链表
剑指 Offer 25. 

[力扣](https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof/) / [Python3](./python-algorithm/sword_point_offer/J25.py) 

## 7 二叉搜索树与双向链表  
剑指 Offer 36. 

[力扣](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/) / [Python3](./python-algorithm/sword_point_offer/J36.py) 


# 二分查找
## 1 二维数组中的查找   
剑指 Offer 04.   

[力扣](https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/) / [Python3](./python-algorithm/sword_point_offer/J04-m.py) 

## 2 旋转数组的最小数字
剑指 Offer 11. 

[力扣](https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/) / [Python3](./python-algorithm/sword_point_offer/J11-m.py) 

## 3 在排序数组中查找数字I 
剑指 Offer 53 - I.    
   
[力扣](https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/) / [Python3](./python-algorithm/sword_point_offer/J53_1.py) 

## 4 0到n-1中缺失的数字
剑指 Offer 53 - II. 

[力扣](https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof/) / [Python3](./python-algorithm/sword_point_offer/J53_2.py) 


# 动态规划
## 1 剪绳子
剑指 Offer 14- I. 

[力扣](https://leetcode-cn.com/problems/jian-sheng-zi-lcof/) / [Python3](./python-algorithm/sword_point_offer/J14-m.py) 
```
题目: 给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 
k[0],k[1]...k[m-1] 。请问 k[0]*k[1]*...*k[m-1]可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成
长度分别为2、3、3的三段，此时得到的最大乘积是18。n>=2。
```

## 2 连续子数组的最大和
剑指 Offer 42. 

[力扣](https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/) / [Python3](./python-algorithm/sword_point_offer/J42.py) 
```
题目: 输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
要求时间复杂度为O(n)。
```

## 3 礼物的最大价值
剑指 Offer 47. 

[力扣](https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof/) / [Python3](./python-algorithm/sword_point_offer/J47.py) 
```
示例 1:
输入: 
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 12
解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物

```

## 4 股票的最大利润
剑指 Offer 63. 

[力扣](https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof/) / [Python3](./python-algorithm/sword_point_offer/J63.py) 
```
题目:假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？
示例 1:
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
```

## 5 n个骰子的点数
剑指 Offer 60. 

[力扣](https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof/) / [Python3](./python-algorithm/sword_point_offer/J60.py) 
```
题目:把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。
你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。

示例 1:
输入: 1
输出: [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]

示例 2:
输入: 2
输出: [0.02778,0.05556,0.08333,0.11111,0.13889,0.16667,0.13889,0.11111,0.08333,0.05556,0.02778]
```




# 股票问题
## 1 买卖股票一次交易
121\. Best Time to Buy and Sell Stock

[力扣](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/) / [Leetcode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) / [Cpp](../algo_05_dynamic_plan/dp_9_stock/L121.cpp) / [Python3](../python-algorithm/algo_05_dynamic_plan/dp_9_stock/L121.py) 
```
题目:给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
    如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
    注意：你不能在买入股票前卖出股票。
示例 1:
      输入: [7,1,5,3,6,4]
      输出: 5
      解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
           注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
```

## 2 买卖股票不限次数
122\. Best Time to Buy and Sell Stock II

[力扣](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/) / [Leetcode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) / [Cpp](../algo_05_dynamic_plan/dp_9_stock/L122.cpp) / [Python3](../python-algorithm/algo_05_dynamic_plan/dp_9_stock/L122.py) 
```
题目: 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
     设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
     注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）
示例 1:
      输入: [7,1,5,3,6,4]
      输出: 7
      解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
           随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
```

## 3 最佳买卖股票时机含冷冻期不限次数
309\. Best Time to Buy and Sell Stock with Cooldown(Medium)

[力扣](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/) / [Leetcode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/) /  [Cpp](../algo_05_dynamic_plan/dp_9_stock/) / [Python3](../python-algorithm/algo_05_dynamic_plan/dp_9_stock/) 
```
题目:给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。
    设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
    你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
    卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
示例:
      输入: [1,2,3,0,2]
      输出: 3 
      解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
```

## 4 买卖股票的最佳时机含手续费不限次数
714\. Best Time to Buy and Sell Stock with Transaction Fee (Medium)

[力扣](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/) / [Leetcode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/) / [Cpp](../algo_05_dynamic_plan/dp_9_stock/) / [Python3](../python-algorithm/algo_05_dynamic_plan/dp_9_stock/) 
```
题目:给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。
    你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
    返回获得利润的最大值。
    注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。
示例 1:
      输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
      输出: 8
      解释: 能够达到的最大利润:  
      在此处买入 prices[0] = 1
      在此处卖出 prices[3] = 8
      在此处买入 prices[4] = 4
      在此处卖出 prices[5] = 9
      总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8
```

## 5 只能进行两次的股票交易
123\. Best Time to Buy and Sell Stock III (Hard)

[力扣](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/description/) / [Leetcode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/) / [Cpp](../algo_05_dynamic_plan/dp_9_stock/) / [Python3](../python-algorithm/algo_05_dynamic_plan/dp_9_stock/) 
```
题目:给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
    设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
    注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
示例 1:
      输入: [3,3,5,0,0,3,1,4]
      输出: 6
      解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
           随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
示例 2:
      输入: [1,2,3,4,5]
      输出: 4
      解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。   
           注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。   
           因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
```

## 6 只能进行k次的股票交易
188\. Best Time to Buy and Sell Stock IV (Hard)

[力扣](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/description/) / [Leetcode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/) / [Cpp](../algo_05_dynamic_plan/dp_9_stock/) / [Python3](../python-algorithm/algo_05_dynamic_plan/dp_9_stock/) 
```
题目:给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
     设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
注意:你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
示例 1:
      输入: [2,4,1], k = 2
      输出: 2
      解释: 在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
示例 2:
      输入: [3,2,6,5,0,3], k = 2
      输出: 7
      解释: 在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
           随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。
```

