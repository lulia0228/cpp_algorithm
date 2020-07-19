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

//思路和141一样
class Solution {
public:
    ListNode* detectCycle(ListNode *head) {
        if(head == NULL || head->next == NULL )
            return NULL ;
        ListNode* fast = head ;
        ListNode* slow = head ;
        while(fast->next != NULL && fast->next->next != NULL){
            fast = fast->next->next ;
            slow = slow->next ;
            if(fast == slow ){
                ListNode* start = head ; //找到快慢指针相遇节点后，再重新到链表头取节点，两个同速度往下走，再相遇就是环的入口
                while(start != fast){
                    start = start->next;
                    fast = fast->next;
                }
                return start ;
            }
        }
        return NULL ;
    }
};

//方法二 哈希法，用集合就好了
#include <set>
class Solution1 {
public:
    ListNode *detectCycle(ListNode *head) {
        if(head == NULL || head->next == NULL ) // 不能用&& 用 ||
            return NULL ;
        set<ListNode *>  p_set ;
        ListNode *p = head ;
        while(p){
            if(p_set.find(p) != p_set.end())
                return p ;
            p_set.insert(p) ;
            p = p->next ;
        }
        return NULL;
    }

};

