<!-- GFM-TOC -->
* [五、树相关](#树相关)
    * [1. 特定深度节点链表](#1-特定深度节点链表)
    * [2. 合法二叉搜索树](#2-合法二叉搜索树)
    * [3. 后继者](#3-后继者)
    * [4. 首个共同祖先](#4-首个共同祖先)
    * [5. 检查子树](#5-检查子树)
    * [6. Trie单词频率](#6-Trie单词频率)
    * [7. Trie多次搜索](#7-Trie次搜索)

* [七、二分查找](#二分查找)


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
