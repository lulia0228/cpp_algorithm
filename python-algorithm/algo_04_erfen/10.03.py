#--coding:utf-8--
class Solution:
    def search(self, arr: List[int], target: int) -> int:
        lt, rt = 0, len(arr)-1
        if arr[0] != arr[-1]:
            while lt <= rt:
                mid = lt +(rt-lt)//2
                if target > arr[-1]: # 目标在左子数组
                    if arr[mid] < arr[-1]: # 中点在右子数组
                        rt = mid - 1
                    else:                  # 中点在左子数组
                        if arr[mid] == target:
                            res = mid
                            while res >= 0 and arr[res] == arr[mid]:
                                res -= 1
                            return res + 1
                        elif target>arr[mid]:
                            lt = mid+1
                        else:
                            rt = mid-1
                else:                 # 目标在右子数组
                    if arr[mid] > arr[-1]: # 中点在左子数组
                        lt = mid + 1
                    else:
                        if arr[mid] == target:
                            res = mid
                            while res >= 0 and arr[res] == arr[mid]:
                                res -= 1
                            return res + 1
                        elif target>arr[mid]:
                            lt = mid+1
                        else:
                            rt = mid-1
        else:  # 处理在连续元素处发生旋转的特殊情况
            while rt >= 0 and arr[rt] == arr[0]:
                rt -= 1
            while lt <= rt:
                mid = lt +(rt-lt)//2
                if target > arr[rt]: # 目标在左子数组
                    if arr[mid] < arr[rt]: # 中点在右子数组
                        rt = mid - 1
                    else:                  # 中点在左子数组
                        if arr[mid] == target:
                            res = mid
                            while res >= 0 and arr[res] == arr[mid]:
                                res -= 1
                            return res + 1
                        elif target>arr[mid]:
                            lt = mid+1
                        else:
                            rt = mid-1
                else:                 # 目标在右子数组
                    if arr[mid] > arr[rt]: # 中点在左子数组
                        lt = mid + 1
                    else:
                        if arr[mid] == target:
                            res = mid
                            while res >= 0 and arr[res] == arr[mid]:
                                res -= 1
                            return res + 1
                        elif target > arr[mid]:
                            lt = mid+1
                        else:
                            rt = mid-1
        return -1
