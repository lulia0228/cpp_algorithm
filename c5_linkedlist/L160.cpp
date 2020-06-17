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