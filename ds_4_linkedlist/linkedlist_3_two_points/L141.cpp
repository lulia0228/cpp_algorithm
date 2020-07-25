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

