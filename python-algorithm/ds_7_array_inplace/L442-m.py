#--coding:utf-8--
'''
要不使用额外内存空间，则只能原地修改数组元素来标记是否访问过
原理：如果是相同的元素，那么以他们为索引的元素值一定是同一个值，
因此可以修改该值来标记是否被访问过
注意：既要原地修改元素，就不能影响其自身作为索引的访问，那么只有一种办法，
那就是将该元素取反，或者加减某个数，在访问的时候，再通过取正或者加减某个数还原回来
'''

from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        rst = []
        for num in nums:
            # 因为我们是直接原地修改元素为负值来标记是否访问过，因此这里的num一定要取绝对值
            index = abs(num) - 1
            val = nums[index]
            if val < 0:
                # 如果元素值为负数，说明之前存在同一个索引为num的元素
                rst.append(abs(num))

            # 原地修改访问标志
            nums[index] = -nums[index]
        return rst


if __name__ == '__main__':
    test = Solution()
    print(test.findDuplicates([4, 3, 2, 7, 8, 7, 3, 1]))

