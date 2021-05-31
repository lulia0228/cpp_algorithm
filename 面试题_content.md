<!-- GFM-TOC -->
* [五、树相关](#树相关)
    * [1. 特定深度节点链表](#1-特定深度节点链表)
    * [2. 合法二叉搜索树](#2-合法二叉搜索树)
    * [3. 后继者](#3-后继者)
    * [4. 首个共同祖先](#4-首个共同祖先)
    * [5. 检查子树](#5-检查子树)
    * [6. Trie单词频率](#6-Trie单词频率)
    * [7. Trie多次搜索](#7-Trie次搜索)

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


* [十、哈希](#哈希)
    * [1. 变位词组](#1-变位词组)
    * [2. 数字流的秩](#2-数字流的秩)
    * [3. 交换和](#3-交换和)
    * [4. 数对和 ](#4-数对和)
    * [5. 字母与数字](#5-字母与数字)
    
* [十一、双指针](#双指针)
    * [1. 最小差](#1-最小差)
    * [2. 部分排序](#2-部分排序)
    * [3. 单词距离](#3-单词距离)
    
* [十二、图的遍历](#图的遍历)
    * [1. 节点间通路](#1-节点间通路)
    * [2. 迷路的机器人](#2-迷路的机器人)
    * [3. 水域大小](#3-水域大小)
    * [4. 单词转换](#4-单词转换)

<!-- GFM-TOC -->

# 树相关
## 1 特定深度节点链表        
面试题 04.03. 特定深度节点链表     

[力扣](https://leetcode-cn.com/problems/list-of-depth-lcci/) / [Python3](./python-algorithm/interview_sets/04.03.py)      
```
给定一棵二叉树，设计一个算法，创建含有某一深度上所有节点的链表（比如，若一棵树的深度为 D，则会创建出 D 个链表）。返回一个包含所有深度的链表的数组。

输入：[1,2,3,4,5,null,7,8]

        1
       /  \ 
      2    3
     / \    \ 
    4   5    7
   /
  8

输出：[[1],[2,3],[4,5,7],[8]]
```

## 2 合法二叉搜索树   
面试题 04.05. 合法二叉搜索树     

[力扣](https://leetcode-cn.com/problems/legal-binary-search-tree-lcci/) / [Python3](./python-algorithm/interview_sets/04.05.py)      
```
实现一个函数，检查一棵二叉树是否为二叉搜索树。

示例 1:
输入:
                      2
                     / \
                    1   3
输出: true

示例 2:
输入:
                   5
                  / \
                 1   4
                    / \
                   3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。

```

## 3 后继者  
面试题 04.06. 后继者       

[力扣](https://leetcode-cn.com/problems/successor-lcci/) / [Python3](./python-algorithm/interview_sets/04.06.py)      
```
设计一个算法，找出二叉搜索树中指定节点的“下一个”节点（也即中序后继）。
如果指定节点没有对应的“下一个”节点，则返回null。

输入: root = [2,1,3], p = 1
           2
          / \
         1   3

输出: 2
```

## 4 首个共同祖先  
面试题 04.08. 首个共同祖先     

[力扣](https://leetcode-cn.com/problems/first-common-ancestor-lcci/) / [Python3](./python-algorithm/interview_sets/04.08.py)      
```
设计并实现一个算法，找出二叉树中某两个节点的第一个共同祖先。不得将其他的节点存储在另外的数据结构中。注意：这不一定是二叉搜索树。
例如，给定如下二叉树: root = [3,5,1,6,2,0,8,null,null,7,4]

    3
   / \
  5   1
 / \ / \
6  2 0  8
  / \
 7   4
示例 1:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
示例 2:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
```

## 5 检查子树   
面试题 04.10. 检查子树   

[力扣](https://leetcode-cn.com/problems/check-subtree-lcci/) / [Python3](./python-algorithm/interview_sets/04.10.py)      
```
检查子树。你有两棵非常大的二叉树：T1，有几万个节点；T2，有几万个节点。设计一个算法，判断 T2 是否为 T1 的子树。
如果 T1 有这么一个节点 n，其子树与 T2 一模一样，则 T2 为 T1 的子树，也就是说，从节点 n 处把树砍断，得到的树与 T2 完全相同。

示例1:

 输入：t1 = [1, 2, 3], t2 = [2]
 输出：true
示例2:

 输入：t1 = [1, null, 2, 4], t2 = [3, 2]
 输出：false
```

## 6 Trie单词频率  
面试题 16.02. 单词频率    

[力扣](https://leetcode-cn.com/problems/words-frequency-lcci/) / [Python3](./python-algorithm/interview_sets/16.02.py)      
```
设计一个方法，找出任意指定单词在一本书中的出现频率。
你的实现应该支持如下操作：

WordsFrequency(book)构造函数，参数为字符串数组构成的一本书
get(word)查询指定单词在书中出现的频率
示例：

WordsFrequency wordsFrequency = new WordsFrequency({"i", "have", "an", "apple", "he", "have", "a", "pen"});
wordsFrequency.get("you"); //返回0，"you"没有出现过
wordsFrequency.get("have"); //返回2，"have"出现2次
wordsFrequency.get("an"); //返回1
wordsFrequency.get("apple"); //返回1
wordsFrequency.get("pen"); //返回1
```

## 7 Trie多次搜索
面试题 17.17. 多次搜索  

[力扣](https://leetcode-cn.com/problems/multi-search-lcci/) / [Python3](./python-algorithm/interview_sets/17.17.py)      
```
给定一个较长字符串big和一个包含较短字符串的数组smalls，设计一个方法，根据smalls中的每一个较短字符串，
对big进行搜索。输出smalls中的字符串在big里出现的所有位置positions，其中positions[i]为smalls[i]出现的所有位置。

输入：
big = "mississippi"
smalls = ["is","ppi","hi","sis","i","ssippi"]
输出： [[1,4],[8],[],[3],[1,4,7,10],[5]]
```

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


# 前缀和思想
## 1 生存人数
面试题 16.10. 生存人数  

[力扣](https://leetcode-cn.com/problems/living-people-lcci/) / [Python3](./python-algorithm/interview_sets/16.06.py) 
```
给定 N 个人的出生年份和死亡年份，第 i 个人的出生年份为 birth[i]，死亡年份为 death[i]，实现一个方法以计算生存人数最多的年份。
你可以假设所有人都出生于 1900 年至 2000 年（含 1900 和 2000 ）之间。如果一个人在某一年的任意时期处于生存状态，
那么他应该被纳入那一年的统计中。例如，生于 1908 年、死于 1909 年的人应当被列入 1908 年和 1909 年的计数。

如果有多个年份生存人数相同且均为最大值，输出其中最小的年份。

输入：
         birth = {1900, 1901, 1950}
         death = {1948, 1951, 2000}
输出： 1901
```


# 哈希
## 1 变位词组
面试题 10.02. 变位词组  

[力扣](https://leetcode-cn.com/problems/group-anagrams-lcci/) / [Python3](./python-algorithm/interview_sets/10.02.py) 
```
编写一种方法，对字符串数组进行排序，将所有变位词组合在一起。变位词是指字母相同，但排列不同的字符串。
注意：本题相对原题稍作修改

输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
输出:
         [
           ["ate","eat","tea"],
           ["nat","tan"],
           ["bat"]
         ]

```

## 2 数字流的秩   
面试题 10.10. 数字流的秩     

[力扣](https://leetcode-cn.com/problems/rank-from-stream-lcci/) / [Python3](./python-algorithm/interview_sets/10.10.py)  
```
假设你正在读取一串整数。每隔一段时间，你希望能找出数字 x 的秩(小于或等于 x 的值的个数)。请实现数据结构和算法来支持这些操作，也就是说：
实现 track(int x) 方法，每读入一个数字都会调用该方法；
实现 getRankOfNumber(int x) 方法，返回小于或等于 x 的值的个数。
注意：本题相对原题稍作改动

输入:
["StreamRank", "getRankOfNumber", "track", "getRankOfNumber"]
[[], [1], [0], [0]]
输出:
[null,0,null,1]

```
## 3 交换和     
面试题 16.21. 交换和       

[力扣](https://leetcode-cn.com/problems/sum-swap-lcci/) / [Python3](./python-algorithm/interview_sets/16.21.py)  
```
给定两个整数数组，请交换一对数值（每个数组中取一个数值），使得两个数组所有元素的和相等。
返回一个数组，第一个元素是第一个数组中要交换的元素，第二个元素是第二个数组中要交换的元素。
若有多个答案，返回任意一个均可。若无满足条件的数值，返回空数组。

示例:
输入: array1 = [4, 1, 2, 1, 1, 2], array2 = [3, 6, 3, 3]
输出: [1, 3]

示例:
输入: array1 = [1, 2, 3], array2 = [4, 5, 6]
输出: []
```

## 4 数对和   
面试题 16.24. 数对和  

[力扣](https://leetcode-cn.com/problems/pairs-with-sum-lcci/) / [Python3](./python-algorithm/interview_sets/16.24.py)  
```
设计一个算法，找出数组中两数之和为指定值的所有整数对。一个数只能属于一个数对。
示例 1:
输入: nums = [5,6,5], target = 11
输出: [[5,6]]

示例 2:
输入: nums = [5,6,5,6], target = 11
输出: [[5,6],[5,6]]
```

## 5 字母与数字   
面试题 17.05.  字母与数字 

[力扣](https://leetcode-cn.com/problems/find-longest-subarray-lcci/) / [Python3](./python-algorithm/interview_sets/17.05.py)  
```
给定一个放有字符和数字的数组，找到最长的子数组，且包含的字符和数字的个数相同。
返回该子数组，若存在多个最长子数组，返回左端点最小的。若不存在这样的数组，返回一个空数组。

输入: ["A","1","B","C","D","2","3","4","E","5","F","G","6","7","H","I","J","K","L","M"]
输出: ["A","1","B","C","D","2","3","4","E","5","F","G","6","7"]
```


# 双指针
## 1 最小差
面试题 16.06. 最小差  

[力扣](https://leetcode-cn.com/problems/smallest-difference-lcci/) / [Python3](./python-algorithm/interview_sets/16.06.py) 
```
给定两个整数数组a和b，计算具有最小差绝对值的一对数值（每个数组中取一个值），并返回该对数值的差

输入：{1, 3, 15, 11, 2}, {23, 127, 235, 19, 8}
输出：3，即数值对(11, 8)
```

## 2 部分排序
面试题 16.16. 部分排序  

[力扣](https://leetcode-cn.com/problems/sub-sort-lcci/) / [Python3](./python-algorithm/interview_sets/16.16.py)  
```
给定一个整数数组，编写一个函数，找出索引m和n，只要将索引区间[m,n]的元素排好序，整个数组就是有序的。
注意：n-m尽量最小，也就是说，找出符合条件的最短序列。函数返回值为[m,n]，若不存在这样的m和n
例如整个数组是有序的），请返回[-1,-1]。

输入： [1,2,4,7,10,11,7,12,6,7,16,18,19]
输出： [3,9]
```


## 3 单词距离  
面试题 17.11. 单词距离   

[力扣](https://leetcode-cn.com/problems/find-closest-lcci/) / [Python3](./python-algorithm/interview_sets/17.11.py)  
```
有个内含单词的超大文本文件，给定任意两个单词，找出在这个文件中这两个单词的最短距离(相隔单词数)。
如果寻找过程在这个文件中会重复多次，而每次寻找的单词不同，你能对此优化吗?

输入：words = ["I","am","a","student","from","a","university","in","a","city"], word1 = "a", word2 = "student"
输出：1
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
