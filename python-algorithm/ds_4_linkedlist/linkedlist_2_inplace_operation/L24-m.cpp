
//leetcode 24 交换链表节点

#include <iostream>
#include <vector>

using namespace std;

struct ListNode {
    int val ;
    ListNode* next ;
    ListNode(int x): val(x) , next(NULL) {}
};

class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        if(head==NULL||head->next == NULL)
            return head;
        ListNode* dummy = new ListNode(-1);
        dummy->next = head;
        ListNode* pre = dummy;
        ListNode* back = head;
        while(head && head->next){
            back = head->next;
            pre->next = back;
            head->next = back->next;
            back->next = head;
            pre = head;
            head = pre->next;
        }
        ListNode* res = dummy->next;
        delete dummy;
        return res;
    }
};


int main(){
    return 0 ;
}

//练习leetcode 25 147(链表插入排序) 148（对链表排序）