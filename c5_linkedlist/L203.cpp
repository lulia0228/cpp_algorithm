//
// Created by liheng on 19-7-23.
//

//leetcode 203
#include <iostream>
#include <vector>

using namespace std;

struct ListNode {
    int val ;
    ListNode* next ;
    ListNode(int x): val(x) , next(NULL) {}
};


class Solution1{
public:
    ListNode* removeElements(ListNode* head , int val){

        if (head == NULL)
            return NULL ;

        ListNode* cur = head ;
        while(cur->next != NULL){
            if (cur->next->val == val ){
                ListNode* delNode = cur->next ;
                cur->next = delNode->next ;
                delete delNode ;
            }
            else
                cur = cur->next ;
        }
        return head ;
    }
};

//Solution1 的逻辑是有问题的。因为对于要删除的元素是首元素的时候，没法通过前面的节点判断。,头结点没有上一个节点。

class Solution2{
public:
    ListNode* removeElements(ListNode* head , int val){

        // 针对头结点 ：陷阱--如果删除了头结点，后面又要删除的又是新形成的头结点。怎么办呢？
        // 解决办法：写成循环，不要写成一个if 判断

        while (head != NULL && head->val == val ){
            ListNode* delNode = head ;
            head = delNode->next;
            delete delNode ;
        }

        // 万一上面循环下来，链表中没有元素了，要写个保护
        if (head == NULL)
            return NULL ;

        ListNode* cur = head ;
        while(cur->next != NULL){
            if (cur->next->val == val ){
                ListNode* delNode = cur->next ;
                cur->next = delNode->next ;
                delete delNode ;
            }
            else
                cur = cur->next ;
        }
        return head ;
    }
};

// Solution2为了处理头结点问题，带来了很多陷阱，有没有办法所有节点统一处理呢
// 解决办法：设置一个虚拟头结点

class Solution3{
public:
    ListNode* removeElements(ListNode* head , int val){

        ListNode* dummyHead = new ListNode(0); //要用结构体类型初始化，确保和链表中其它节点类型一样
        dummyHead->next = head ;
        ListNode* cur = dummyHead ;

        while(cur->next != NULL){
            if (cur->next->val == val ){
                ListNode* delNode = cur->next ;
                cur->next = delNode->next ;
                delete delNode ;
            }
            else
                cur = cur->next ;
        }
        ListNode* retNode = dummyHead->next ;
        delete dummyHead ; //因为采用了new  所以要释放内存 防止内存泄露

        return retNode ;
    }
};


int main(){

    return 0 ;
}

//练习 leetcode 82 21