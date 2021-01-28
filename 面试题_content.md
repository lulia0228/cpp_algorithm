<!-- GFM-TOC -->
* [一、栈和队列](#栈和队列)
    * [1. 栈排序](#1-栈排序)

* [二、滑动窗口](#滑动窗口)
    * [1. 最短超串](#1-最短超串)  
   
* [三、堆的应用](#堆的应用)
    * [1. 最小的k个数 ](#1-最小的k个数 )  

* [四、位运算](#位运算)
    * [1. 交换数字](#1-交换数字)
 
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
    * [1. 分割链表](#1-分割链表)
    * [2. 链表求和](#2-链表求和)
    * [3. 环路检测](#3-环路检测)
  
* [七、二分查找](#二分查找)
    * [1. 搜索旋转数组](#1-搜索旋转数组)
    * [2. 排序矩阵查找](#2-排序矩阵查找)


* [八、动态规划](#动态规划)
    * [1. 一次编辑](#1-一次编辑)
    * [2. 硬币](#2-硬币)
    * [3. 马戏团人塔](#3-马戏团人塔)
    * [4. 丑数](#4-丑数)   
    * [5. 恢复空格](#5-恢复空格)  
    * [6. 最长单词](#6-最长单词)  
    * [7. 最大黑方阵](#7-最大黑方阵)  

* [九、分治](#分治)
    * [1. 数组中的逆序对](#1-数组中的逆序对)
    * [2. 二叉搜索树的后序遍历序列](#2-二叉搜索树的后序遍历序列)
 
* [十、图的遍历](#图的遍历)
    * [1. 节点间通路](#1-节点间通路)
    * [2. 迷路的机器人](#2-迷路的机器人)
    * [3. 水域大小](#3-水域大小)
    * [4. 单词转换](#4-单词转换)

<!-- GFM-TOC -->


# 栈和队列
## 1 栈排序  
面试题 03.05. 栈排序 

[力扣](https://leetcode-cn.com/problems/sort-of-stacks-lcci/) / [Python3](./python-algorithm/interview_sets/03.05.py)     
```
栈排序。 编写程序，对栈进行排序使最小元素位于栈顶。最多只能使用一个其他的临时栈存放数据，但不得将元素复制到别的数据结构（如数组）中。
该栈支持如下操作：push、pop、peek 和 isEmpty。当栈为空时，peek 返回 -1。

输入：
["SortedStack", "push", "push", "peek", "pop", "peek"]
[[], [1], [2], [], [], []]
输出：
[null,null,null,1,null,2]

```

# 滑动窗口  
## 1 最短超串
面试题 17.18. 最短超串     

[力扣](https://leetcode-cn.com/problems/shortest-supersequence-lcci/) / [Python3](./python-algorithm/interview_sets/17.18.py) 
```
假设你有两个数组，一个长一个短，短的元素均不相同。找到长数组中包含短数组所有的元素的最短子数组，其出现顺序无关紧要。
返回最短子数组的左端点和右端点，如有多个满足条件的子数组，返回左端点最小的一个。若不存在，返回空数组。

输入:
big = [7,5,9,0,2,1,3,5,7,9,1,1,5,8,8,9,7]
small = [1,5,9]
输出: [7,10] 
```


# 堆的应用   
## 1 最小的k个数  
面试题 17.14. 最小K个数    

[力扣](https://leetcode-cn.com/problems/smallest-k-lcci/) / [Python3](./python-algorithm/interview_sets/17.14.py)     
```
设计一个算法，找出数组中最小的k个数。以任意顺序返回这k个数均可。

示例：
输入： arr = [1,3,5,7,2,4,6,8], k = 4
输出： [1,2,3,4]
```


# 位运算
## 1 交换数字
面试题 16.01. 交换数字          

[力扣](https://leetcode-cn.com/problems/swap-numbers-lcci/) / [Python3](./python-algorithm/interview_sets/16.01.py)      
```
编写一个函数，不用临时变量，直接交换numbers = [a, b]中a与b的值。

示例：
输入: numbers = [1,2]
输出: [2,1]
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
## 1 分割链表  
面试题 02.04. 分割链表     

[力扣](https://leetcode-cn.com/problems/partition-list-lcci/) / [Python3](./python-algorithm/interview_sets/02.04.py) 
```
编写程序以 x 为基准分割链表，使得所有小于 x 的节点排在大于或等于 x 的节点之前。如果链表中包含 x，x 只需出现在小于
x 的元素之后(如下所示)。分割元素 x 只需处于“右半部分”即可，其不需要被置于左右两部分之间。

示例:
输入: head = 3->5->8->5->10->2->1, x = 5
输出: 3->1->2->10->5->5->8
```

## 2 链表求和
面试题 02.05. 链表求和     

[力扣](https://leetcode-cn.com/problems/sum-lists-lcci/) / [Python3](./python-algorithm/interview_sets/02.05.py) 
```
给定两个用链表表示的整数，每个节点包含一个数位。
这些数位是反向存放的，也就是个位排在链表首部。
编写函数对这两个整数求和，并用链表形式返回结果。

示例：
输入：(7 -> 1 -> 6) + (5 -> 9 -> 2)，即617 + 295
输出：2 -> 1 -> 9，即912
```

## 3 环路检测
面试题 02.08. 环路检测    
   
[力扣](https://leetcode-cn.com/problems/linked-list-cycle-lcci/) / [Python3](./python-algorithm/interview_sets/02.08.py) 
```
给定一个链表，如果它是有环链表，实现一个算法返回环路的开头节点。
如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，我们使用整数 pos 
来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
```


# 二分查找
## 1 搜索旋转数组    
面试题 10.03. 搜索旋转数组   

[力扣](https://leetcode-cn.com/problems/search-rotate-array-lcci/) / [Python3](./python-algorithm/interview_sets/10.03.py) 
```
搜索旋转数组。给定一个排序后的数组，包含n个整数，但这个数组已被旋转过很多次了，次数不详。请编写代码找出数组中的某个元素，
假设数组元素原先是按升序排列的。若有多个相同元素，返回索引值最小的一个。

示例1:
 输入: arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], target = 5
 输出: 8（元素5在该数组中的索引）
```

## 2 排序矩阵查找  
面试题 10.09. 排序矩阵查找   

[力扣](https://leetcode-cn.com/problems/sorted-matrix-search-lcci/) / [Python3](./python-algorithm/interview_sets/10.09.py) 
```
给定M×N矩阵，每一行、每一列都按升序排列，请编写代码找出某元素。

示例:
现有矩阵 matrix 如下：
      [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
      ]
给定 target = 5，返回 true。
给定 target = 20，返回 false。
```

# 动态规划
## 1 一次编辑  
面试题 01.05. 一次编辑   

[力扣](https://leetcode-cn.com/problems/one-away-lcci/) / [Python3](./python-algorithm/interview_sets/01.05.py) 
```
字符串有三种编辑操作:插入一个字符、删除一个字符或者替换一个字符。 给定两个字符串，编写一个函数判定它们是否只需要一次(或者零次)编辑。

输入: 
      first = "pale"
      second = "ple"
输出:   True
```

## 2 硬币   
面试题 08.11. 硬币   

[力扣](https://leetcode-cn.com/problems/coin-lcci/) / [Python3](./python-algorithm/interview_sets/08.11.py) 
```
硬币。给定数量不限的硬币，币值为25分、10分、5分和1分，编写代码计算n分有几种表示法。(结果可能会很大，你需要将结果模上1000000007)

 输入: n = 5
 输出：2
 解释: 有两种方式可以凑成总金额:
         5=5
         5=1+1+1+1+1
```

## 3 马戏团人塔   
面试题 17.08. 马戏团人塔   

[力扣](https://leetcode-cn.com/problems/circus-tower-lcci/) / [Python3](./python-algorithm/interview_sets/17.08.py) 
```
有个马戏团正在设计叠罗汉的表演节目，一个人要站在另一人的肩膀上。出于实际和美观的考虑，在上面的人要比下面的人矮一点且轻一点。
已知马戏团每个人的身高和体重，请编写代码计算叠罗汉最多能叠几个人。

示例：
输入：height = [65,70,56,75,60,68] weight = [100,150,90,190,95,110]
输出：6
解释：从上往下数，叠罗汉最多能叠 6 层：(56,90), (60,95), (65,100), (68,110), (70,150), (75,190)
```

## 4 丑数
面试题 17.09. 第 k 个数  

[力扣](https://leetcode-cn.com/problems/get-kth-magic-number-lcci/) / [Python3](./python-algorithm/interview_sets/17.09.py) 
```
有些数的素因子只有 3，5，7，请设计一个算法找出第 k 个数。注意，不是必须有这些素因子，而是必须不包含其他的素因子。
例如，前几个数按顺序应该是 1，3，5，7，9，15，21。

示例 1:
输入: k = 5
输出: 9
```

## 5 恢复空格  
面试题 17.13. 恢复空格  

[力扣](https://leetcode-cn.com/problems/re-space-lcci/) / [Python3](./python-algorithm/interview_sets/17.13.py) 
```
哦，不！你不小心把一个长篇文章中的空格、标点都删掉了，并且大写也弄成了小写。像句子"I reset the computer. It still didn’t boot!"已经
变成了"iresetthecomputeritstilldidntboot"。在处理标点符号和大小写之前，你得先把它断成词语。当然了，你有一本厚厚的词典dictionary，
不过，有些词没在词典里。假设文章用sentence表示，设计一个算法，把文章断开，要求未识别的字符最少，返回未识别的字符数。

注意：本题相对原题稍作改动，只需返回未识别的字符数

输入：
dictionary = ["looked","just","like","her","brother"]
sentence = "jesslookedjustliketimherbrother"
输出： 7
解释： 断句后为"jess looked just like tim her brother"，共7个未识别字符。
```

## 6 最长单词  
面试题 17.15. 最长单词   

[力扣](https://leetcode-cn.com/problems/longest-word-lcci/) / [Python3](./python-algorithm/interview_sets/17.15.py) 
```
给定一组单词words，编写一个程序，找出其中的最长单词，且该单词由这组单词中的其他单词组合而成。若有多个长度相同的结果，
返回其中字典序最小的一项，若没有符合要求的单词则返回空字符串。

输入： ["cat","banana","dog","nana","walk","walker","dogwalker"]
输出： "dogwalker"
解释： "dogwalker"可由"dog"和"walker"组成。
```


## 7 最大黑方阵 
面试题 17.23. 最大黑方阵   

[力扣](https://leetcode-cn.com/problems/max-black-square-lcci/) / [Python3](./python-algorithm/interview_sets/17.23.py) 
```
给定一个方阵，其中每个单元(像素)非黑即白。设计一个算法，找出 4 条边皆为黑色像素的最大子方阵。
返回一个数组 [r, c, size] ，其中 r, c 分别代表子方阵左上角的行号和列号，size 是子方阵的边长。
若有多个满足条件的子方阵，返回 r 最小的，若 r 相同，返回 c 最小的子方阵。
若无满足条件的子方阵，返回空数组。

输入:
         [
            [1,0,1],
            [0,0,1],
            [0,0,1]
         ]
输出: [1,0,2]
解释: 输入中 0 代表黑色，1 代表白色，标粗的元素即为满足条件的最大子方阵
```


# 分治
## 1 数组中的逆序对
剑指 Offer 51. 

[力扣](https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/) / [Python3](./python-algorithm/sword_point_offer/J51-h.py) 
```
题目:在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。
示例 1:
输入: [7,5,6,4]
输出: 5
```

## 2 二叉搜索树的后序遍历序列
剑指 Offer 33. 

[力扣](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/) / [Python3](./python-algorithm/sword_point_offer/J33-m.py)  
```
题目: 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，
否则返回 false。假设输入的数组的任意两个数字都互不相同。
参考以下这颗二叉搜索树：
           5
          / \
         2   6
        / \
       1   3
示例 1：
      输入: [1,6,3,2,5]
      输出: false
```

# 图的遍历
## 1 节点间通路
面试题 04.01. 节点间通路   

[力扣](https://leetcode-cn.com/problems/route-between-nodes-lcci/) / [Python3](./python-algorithm/interview_sets/04.01.py) 
```
节点间通路。给定有向图，设计一个算法，找出两个节点之间是否存在一条路径。

示例1:
输入：n = 3, graph = [[0,1], [0,2], [1,2], [1,2]], start = 0, target=2
输出：true
示例2:
输入：n = 5, graph = [[0,1], [0,2], [0,4], [0,4], [0,1], [1,3], [1,4], [1,3], [2,3], [3,4]], start=0, target=4
输出 true

```

## 2 迷路的机器人
面试题 08.02. 迷路的机器人   

[力扣](https://leetcode-cn.com/problems/robot-in-a-grid-lcci/) / [Python3](./python-algorithm/interview_sets/08.02.py) 
```
设想有个机器人坐在一个网格的左上角，网格 r 行 c 列。机器人只能向下或向右移动，但不能走到一些被禁止的网格（有障碍物）。
设计一种算法，寻找机器人从左上角移动到右下角的路径。

网格中的障碍物和空位置分别用 1 和 0 来表示。
返回一条可行的路径，路径由经过的网格的行号和列号组成。左上角为 0 行 0 列。如果没有可行的路径，返回空数组。
```

## 3 水域大小
面试题 16.19. 水域大小     

[力扣](https://leetcode-cn.com/problems/pond-sizes-lcci/) / [Python3](./python-algorithm/interview_sets/16.19.py) 
```
你有一个用于表示一片土地的整数矩阵land，该矩阵中每个点的值代表对应地点的海拔高度。若值为0则表示水域。由垂直、水平或对角连接的水域为池塘。
池塘的大小是指相连接的水域的个数。编写一个方法来计算矩阵中所有池塘的大小，返回值需要从小到大排序。

输入：
         [
           [0,2,1,0],
           [0,1,0,1],
           [1,1,0,1],
           [0,1,0,1]
         ]
输出：      [1,2,4]

```


## 4 单词转换
面试题 17.22. 单词转换   

[力扣](https://leetcode-cn.com/problems/word-transformer-lcci/) / [Python3](./python-algorithm/interview_sets/17.22.py) 
```
给定字典中的两个词，长度相等。写一个方法，把一个词转换成另一个词， 但是一次只能改变一个字符。每一步得到的新词都必须能在字典中找到。
编写一个程序，返回一个可能的转换序列。如有多个可能的转换序列，你可以返回任何一个。

示例 1:
输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
输出:
["hit","hot","dot","lot","log","cog"]

示例 2:
输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
输出: []
解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。
```
