

//leetcode 203 移除链表中所有值等于给定值的节点
#include <iostream>
using namespace std;

struct ListNode {
    int val ;
    ListNode* next ;
    ListNode(int x): val(x) , next(NULL) {}
};

class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        ListNode* dummy = new ListNode(-1);
        dummy->next = head;
        ListNode* pre = dummy; //标记上个节点
        ListNode* cur = head;
        while(cur){
            if(cur->val == val){
                pre->next = cur->next;
                cur = cur->next;
            }
            else{
                pre = cur;
                cur = cur->next;
            }
        }
        return dummy->next;
    }
};


int main(){

    return 0 ;
}

//练习 leetcode 82 21