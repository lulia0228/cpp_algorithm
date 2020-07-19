//
// Created by LiHeng on 2020/4/19.
//
#include <iostream>
using namespace std;

//  Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

// 题目要求不能修改原来的链表结构，不能占用额外空间，因此反转链表和哈希查找法不符合要求
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode* ha = headA;
        ListNode* hb = headB;

        while(ha != hb){ // 如果不相交，二者各走一遍对方的路，最终会同时还走向对方的终点都是空也会退出循环
            ha = (ha == NULL? headB:ha->next);
            hb = (hb == NULL? headA:hb->next);
        }
        return ha;
    }
};