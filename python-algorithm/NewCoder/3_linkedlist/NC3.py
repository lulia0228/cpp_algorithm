

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self , head ):
        # write code here
        if not head : return None
        flag = False
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                flag = True
                break

        if flag:
            start = head
            while start!=slow:
                start = start.next
                slow = slow.next
            return start
        else:
            return None


# 哈希
class Solution:
    def detectCycle(self , head ):
        # write code here
        if not head: return None
        st = set()
        while head:
            if head in st: return head
            st.add(head)
            head = head.next
        return None