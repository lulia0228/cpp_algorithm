<!-- GFM-TOC -->
* [一、栈和队列](#栈和队列)
    * [1. 用两个栈实现队列](#1-用两个栈实现队列)
    * [2. 包含min函数的栈](#2-包含min函数的栈)
    * [3. 队列的最大值](#3-队列的最大值)   

* [二、堆的应用](#堆的应用)
    * [1. 最小的k个数 ](#1-最小的k个数 )
    * [2. 数据流中的中位数](#2-数据流中的中位数)
    
* [三、位运算](#位运算)
    * [1. 二进制中1的个数](#1-二进制中1的个数)
    * [2. 数组中出现次数超过一半的数字](#2-数组中出现次数超过一半的数字)
    
* [四、树相关](#树相关)
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

* [五、链表相关](#链表相关)
    * [1. 从尾到头打印链表](#1-从尾到头打印链表)
    * [2. 删除链表的节点](#2-删除链表的节点)
    * [3. 链表中倒数第k个节点](#3-链表中倒数第k个节点)
    * [4. 反转链表](#4-反转链表)
    * [5. 两个链表的第一个公共节点](#5-两个链表的第一个公共节点)
    
* [六、二分查找](#二分查找)
    * [1. 二维数组中的查找](#1-二维数组中的查找)
    * [2. 旋转数组的最小数字](#2-旋转数组的最小数字)
    * [3. 在排序数组中查找数字I](#3-在排序数组中查找数字I)
    * [4. 0到n-1中缺失的数字](#4-0到n-1中缺失的数字)

    
* [六、特殊状态转移方程](#特殊状态转移方程)
    * [1. 格雷编码](#1-格雷编码)
    * [2. 比特位计数](#2-比特位计数)
    * [3. 解码方法](#3-解码方法)
    * [4. 复制粘贴字符](#4-复制粘贴字符)
    * [5. 整数拆分](#5-整数拆分)
    * [6. 整数拆分成最少平方数之和](#6-整数拆分成最少平方数之和)
    * [7. 不同的二叉搜索树  ](#7-不同的二叉搜索树) 

    
* [矩形问题](#矩形问题)
   * [1. 最大正方形](#1-最大正方形)
   * [2. 最大矩形](#2-最大矩形)
   
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




# 特殊状态转移方程
## 1 格雷编码
89\. Gray Code

[力扣](https://leetcode-cn.com/problems/gray-code/) / [Leetcode](https://leetcode.com/problems/gray-code/) / [Cpp](../algo_05_dynamic_plan/dp_4_special_state_transition/L89-m.cpp) / [Python3](../python-algorithm/algo_05_dynamic_plan/dp_4_special_state_transition/L89-m.py)   
```
题目: 格雷编码是一个二进制数字系统，在该系统中，两个连续的数值仅有一个位数的差异。
     给定一个代表编码总位数的非负整数 n，打印其格雷编码序列。即使有多个不同答案，你也只需要返回其中一种。
     格雷编码序列必须以 0 开头。
示例 1:
      输入: 2
      输出: [0,1,3,2]
      解释:
      00 - 0
      01 - 1
      11 - 3
      10 - 2

      对于给定的 n，其格雷编码序列并不唯一。
      例如，[0,2,3,1] 也是一个有效的格雷编码序列。

      00 - 0
      10 - 2
      11 - 3
      01 - 1
```

## 2 比特位计数
338\. Counting Bits

[力扣](https://leetcode-cn.com/problems/counting-bits/) / [Leetcode](https://leetcode.com/problems/counting-bits/) / [Cpp](../algo_05_dynamic_plan/dp_4_special_state_transition/L338-m.cpp) / [Python3](../python-algorithm/algo_05_dynamic_plan/dp_4_special_state_transition/L338-m.py) 
```
题目: 给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。
进阶:
      给出时间复杂度为O(n*sizeof(integer))的解答非常容易。但你可以在线性时间O(n)内用一趟扫描做到吗？
      要求算法的空间复杂度为O(n)
```

## 3 解码方法
91\. Decode Ways (Medium)

[力扣](https://leetcode-cn.com/problems/decode-ways/description/) / [Leetcode](https://leetcode.com/problems/decode-ways/description/) / [Cpp](../algo_05_dynamic_plan/dp_4_special_state_transition/L91-m.cpp) / [Python3](../python-algorithm/algo_05_dynamic_plan/dp_4_special_state_transition/L91-m.py) 
```
题目:一条包含字母 A-Z 的消息通过以下方式进行了编码：
   'A' -> 1
   'B' -> 2
   ...
   'Z' -> 26
   给定一个只包含数字的非空字符串，请计算解码方法的总数。

示例 1:
      输入: "12"
      输出: 2
      解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
      示例 2:

      输入: "226"
      输出: 3
      解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 
```

## 4 复制粘贴字符
650\. 2 Keys Keyboard (Medium)

[力扣](https://leetcode-cn.com/problems/2-keys-keyboard/description/) / [Leetcode](https://leetcode.com/problems/2-keys-keyboard/description/) / [Cpp](../algo_05_dynamic_plan/dp_4_special_state_transition/L650-m.cpp) / [Python3](../python-algorithm/algo_05_dynamic_plan/dp_4_special_state_transition/L650-m.py) 
```
题目: 最初在一个记事本上只有一个字符 'A'。你每次可以对这个记事本进行两种操作：
     Copy All (复制全部) : 你可以复制这个记事本中的所有字符(部分的复制是不允许的)。
     Paste (粘贴) : 你可以粘贴你上一次复制的字符。
给定一个数字 n 。你需要使用最少的操作次数，在记事本中打印出恰好 n 个 'A'。输出能够打印出 n 个 'A' 的最少操作次数。
示例 1:
      输入: 3
      输出: 3
      解释:
      最初, 我们只有一个字符 'A'。
      第 1 步, 我们使用 Copy All 操作。
      第 2 步, 我们使用 Paste 操作来获得 'AA'。
      第 3 步, 我们使用 Paste 操作来获得 'AAA'。
```

## 5 整数拆分
343\. Integer Break (Medim)

[力扣](https://leetcode-cn.com/problems/integer-break/description/) / [Leetcode](https://leetcode.com/problems/integer-break/description/) / [Cpp](../algo_05_dynamic_plan/dp_4_special_state_transition/L343.cpp) / [Python3](../python-algorithm/algo_05_dynamic_plan/dp_4_special_state_transition/L343.py) 
```
题目: 给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。
示例 1:
      输入: 2
      输出: 1
      解释: 2 = 1 + 1, 1 × 1 = 1。
      示例 2:

      输入: 10
      输出: 36
      解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
      说明: 你可以假设 n 不小于 2 且不大于 58。
```

## 6 整数拆分成最少平方数之和
279\. Perfect Squares(Medium)

[力扣](https://leetcode-cn.com/problems/perfect-squares/description/) / [Leetcode](https://leetcode.com/problems/perfect-squares/description/) / [Cpp](../algo_05_dynamic_plan/dp_4_special_state_transition/L279-m.cpp) / [Python3](../python-algorithm/algo_05_dynamic_plan/dp_4_special_state_transition/L279-m.py) 
```
题目: 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
示例 1:
      输入: n = 12
      输出: 3 
      解释: 12 = 4 + 4 + 4.
```

## 7 不同的二叉搜索树
96\. Unique Binary Search Trees

[力扣](https://leetcode-cn.com/problems/unique-binary-search-trees/) / [Leetcode](https://leetcode.com/problems/unique-binary-search-trees/) / [Cpp](../algo_05_dynamic_plan/dp_4_special_state_transition/L96-m.cpp) / [Python3](../python-algorithm/algo_05_dynamic_plan/dp_4_special_state_transition/L96-m.py) 
```
题目: 给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
示例:
            输入: 3
            输出: 5
            解释:
            给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

               1         3     3      2      1
                \       /     /      / \      \
                 3     2     1      1   3      2
                /     /       \                 \
               2     1         2                 3
```

# 矩形问题  
## 1 最大正方形
221\. Maximal Square

[力扣](https://leetcode-cn.com/problems/maximal-square/) / [Leetcode](https://leetcode.com/problems/maximal-square/) / [Cpp](../algo_05_dynamic_plan/dp_8_max_matrix/L221-m.cpp) / [Python3](../python-algorithm/algo_05_dynamic_plan/dp_8_max_matrix/L221-m.py) 
```
题目:在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。
示例:
      输入: 
      1 0 1 0 0
      1 0 1 1 1
      1 1 1 1 1
      1 0 0 1 0
      输出: 4
```

## 2 最大矩形
85\. Maximal Rectangle (hard)

[力扣](https://leetcode-cn.com/problems/maximal-rectangle/) / [Leetcode](https://leetcode.com/problems/maximal-rectangle/) / [Cpp](../algo_05_dynamic_plan/dp_8_max_matrix/L85-h.cpp) / [Python3](../python-algorithm/algo_05_dynamic_plan/dp_8_max_matrix/L85-h.py) 
```
题目:给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
示例:
      输入:
      [
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]
      ]
      输出: 6
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

