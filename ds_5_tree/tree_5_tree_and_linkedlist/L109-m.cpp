
#include <iostream>
#include <vector>
using  namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

// 1  时间复杂度是NlogN 空间复杂度是logN
class Solution {
public:
    TreeNode* sortedListToBST(ListNode* head) {
        if(head == NULL) return NULL;
        ListNode* pre = NULL;
        ListNode* slow = head;
        ListNode* fast = head;
        //找到链表中间节点
        while(fast->next && fast->next->next){
            pre = slow; //标记中点前一个链节点
            slow = slow->next;
            fast = fast->next->next;
        }
        // Handling the case when slowPtr was equal to head.
        if (pre)
            pre->next = NULL; //断开链表
        ListNode* new_start = slow->next;
        TreeNode* root = new TreeNode(slow->val);
        //pre = NULL说明中间节点恰好就是链表头节点,特殊处理
        root->left = pre == NULL? NULL:sortedListToBST(head);
        root->right = sortedListToBST(new_start);
        return root;
    }

};

// 2 转成108的有序数组构造二叉搜索树
// 时间复杂度O(N) 空间复杂度O(N)
class Solution1 {
public:
    TreeNode* sortedListToBST(ListNode* head) {
        vector<int> v;
        while(head != NULL){
            v.push_back(head->val);
            head = head->next;
        }
        return DFS(v, 0, v.size()-1);
    }
    TreeNode* DFS(vector<int>& v, int begin, int end){
        if(begin > end) return nullptr;
        int mid = begin+(end-begin)/2;
        TreeNode * root = new TreeNode(v[mid]);
        root->left = DFS(v, begin, mid-1);
        root->right = DFS(v, mid+1, end);
        return root;
    }
};