#--coding:utf-8--


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        cur = dummy
        tmp_l1, tmp_l2 = [], []
        while l1 != None:
            tmp_l1.append(l1.val)
            l1 = l1.next
        while l2 != None:
            tmp_l2.append(l2.val)
            l2 = l2.next
        carry = 0
        while tmp_l1 != [] or tmp_l2 != []:
            tmp_sum = 0
            if tmp_l1 != []:
                tmp_sum += tmp_l1[-1]
                tmp_l1.pop()
            if tmp_l2 != []:
                tmp_sum += tmp_l2[-1]
                tmp_l2.pop()
            tmp_sum += carry
            # 链表头插法的应用
            tmp_node = ListNode(tmp_sum % 10)
            tmp_node.next = cur.next
            cur.next = tmp_node
            carry = tmp_sum // 10  # python整除(取模)用// c++是/
        if carry:
            tmp_node = ListNode(1)
            tmp_node.next = cur.next
            cur.next = tmp_node
        return dummy.next


if __name__ == "__main__":
    ln1 = ListNode(7)
    p = ln1
    for i in [2,4,3]:
        p.next = ListNode(i)
        p = p.next

    ln2 = ListNode(5)
    q = ln2
    for i in [6,4]:
        q.next = ListNode(i)
        q = q.next

    res = Solution().addTwoNumbers(ln1, ln2)
    while res != None:
        print(res.val)
        res = res.next
