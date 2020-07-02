//
// Created by LiHeng on 2020/4/19.
//

//判是否是环形链表

#include <iostream>
using namespace std;

//  Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

//方法1 快慢指针法:注意快慢指针法只是利用只要有环，一定会相遇，但相遇节点并不一定是环的入口
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if(head == NULL || head->next == NULL )
            return false ;
        ListNode* fast = head ;
        ListNode* slow = head ;
        while(fast->next != NULL && fast->next->next != NULL){
            fast = fast->next->next ;
            slow = slow->next ;
            if(fast == slow )
                return true ;
        }
        return false ;
    }
};


//采用哈希法，这里用集合就行了
#include <set>
class Solution1 {
public:
    bool hasCycle(ListNode *head){
        if(head == NULL || head->next == NULL ) //不能用&& 用||
            return false ;
        set<ListNode *>  p_set ;
        ListNode *p = head ;
        while(p){
            if(p_set.find(p) != p_set.end())
                return true ;
            p_set.insert(p) ;
            p = p->next ;
        }
        return false ;
    }
};

class Solution2{
public:
    //leetcode 141 判断环形链表
    //思路:1：快慢指针，既然有一个环形存在，那可以把快慢指针 看做两个运动员围绕操场跑，快的最后总会和慢的相遇；
    //这种思路只能判断有无环 但是不能确定环的位置
    bool hasCycle(ListNode *head) {
        if(head == NULL || head->next == NULL ) //不能用&& 用 ||
            return false ;
        ListNode* fast = head ;
        ListNode* slow = head ;
        while(fast->next != NULL && fast->next->next != NULL){
            fast = fast->next->next ;
            slow = slow->next ;
            if(fast == slow )
                return true ;
        }
        return false ;
    }

    //思路2：用关联容器set来实现，利用set实现
    //用指针p遍历链表。p为空则说明无环，结束循环，返回false；不为空，则判断p是否在p_set中，
    //如果在集合内，则说明存在环，返回true，否则将p插入集合内。

    bool hasCycle2(ListNode *head){
        if(head == NULL || head->next == NULL ) //不能用&& 用||
            return false ;
        set<ListNode *>  p_set ;
        ListNode *p = head ;
        while(p){
            if(p_set.find(p) != p_set.end())
                return true ;
            p_set.insert(p) ;
            p = p->next ;
        }
        return false ;
    }