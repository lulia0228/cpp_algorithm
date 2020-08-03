//
// Created by liheng on 19-8-5.
//

//leetcode 237 这道题比较好玩，注意考察的点，并不是要我们去遍历链表删除节点

// 给定链表中的一个节点，将其删除；和前面的区别在于不是给出一个具体的值和链表本身，只是给出了要删除的节点
// 解决办法:用给定节点的下一个节点的值覆盖给定的节点，并将下一个节点从链表中移除。


#include <iostream>
using namespace std ;

struct ListNode {
    int val ;
    ListNode* next ;
    ListNode(int x): val(x) , next(NULL) {}
};

class Solution {
public:
    void deleteNode(ListNode* node) {
        //ListNode* tem = node->next;
        node->val = node->next->val;
        node->next = node->next->next;
        //delete tem;
    }
};


int main(){
    return 0 ;
}
