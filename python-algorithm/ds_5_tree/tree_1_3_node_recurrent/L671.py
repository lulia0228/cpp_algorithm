#--coding:utf-8--
'''
@Time   : 2020/10/14
@Author : No Name
'''

# 土方法：全部遍历找
class Solution:

    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if root == None:
            return -1
        res = []
        self.travel(root, res)
        res.sort()
        print(res)
        if res[0] == res[-1]:
            return -1
        else:
            i = 1
            while res[i] == res[0]:
                i += 1
            return res[i]

    def travel(self, root, res):
        if root == None:
            return
        res.append(root.val)
        self.travel(root.left, res)
        self.travel(root.right, res)


class Solution:

    def findSecondMinimumValue(self, root: TreeNode) -> int:

        if root.left == None: # 说明遇到叶子节点
            return -1
        leftVal = root.left.val
        rightVal = root.right.val
        if leftVal == root.val:
            leftVal = self.findSecondMinimumValue(root.left);
        if rightVal == root.val:
            rightVal = self.findSecondMinimumValue(root.right);
        #  第2小的值一定是有子节点的
        if leftVal != -1 and rightVal != -1:
            return min(leftVal, rightVal)
        if leftVal != -1:
            return leftVal
        return rightVal

