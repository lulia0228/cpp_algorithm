# -*- coding: utf-8 -*-
'''描述
数组小和的定义如下：
例如，数组s = [1, 3, 5, 2, 4, 6]，在s[0]的左边小于或等于s[0]的数的和为0；在s[1]的左边小于或等于s[1]的数的和为1；在s[2]的左边小于或等于s[2]的数的和为1+3=4；在s[3]的左边小于或等于s[3]的数的和为1；
在s[4]的左边小于或等于s[4]的数的和为1+3+2=6；在s[5]的左边小于或等于s[5]的数的和为1+3+5+2+4=15。所以s的小和为0+1+4+1+6+15=27
给定一个数组s，实现函数返回s的小和
[要求]
时间复杂度为O(nlogn)O(nlogn)，空间复杂度为O(n)O(n)
输入描述：
第一行有一个整数N。表示数组长度
接下来一行N个整数表示数组内的数
'''

'''
# 解题思路：
最容易想到的做法是遍历一遍数组，对于每个元素计算前面比它小的数的和，累加即可得出结果，时间复杂度是O(N²)。
本题的更好的算法是借助 「归并排序」的思路。smallSum([1,3,4,2,5])实际就等于smallSum([1,3,4])+smallSum([2,5])+c。
之所以还有个c，是因为左半段数组中可能存在比右半段数组小的元素，这个不能遗漏。通过归并排序的merge过程，我们可以很方便计算这个c。
在merge时，左段数组L和右段数组R都是有序的了。结合下边的示意图，
当L[i]<=R[j]时，表示L[i]比R[j]~R[r]的元素都要小。因此c需加上j及以后元素的个数*L[i]，即c+=(r-j+1) * L[i]。
'''
'''
#include <iostream>
using namespace std;
typedef long long LL;
const int N = 1e5 + 10;
int nums[N];
int temp[N];
//long long是因为结果可能爆int
LL merge(int a[], int l, int mid, int r)
{
    int i = l, j = mid + 1, k = 0;
    LL res = 0;
    while (i <= mid && j <= r)
    {
        if (a[i] <= a[j])
        {
            res += (r - j + 1) * a[i];
            temp[k++] = a[i++];
        }
        else temp[k++] = a[j++];
    }
    while (i <= mid) temp[k++] = a[i++];
    while (j <= r) temp[k++] = a[j++];
    for (i = l, k = 0; i <= r; i++)
        a[i] = temp[k++];
    return res;
}

LL getSmallSum(int a[], int l, int r)
{
    if (l == r) return 0;
    int mid = (l + r) / 2; 
    LL L = getSmallSum(a, l, mid), R = getSmallSum(a, mid + 1, r);
    LL c = merge(a, l, mid, r);
    return L + R + c;
}

int main()
{
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) cin >> nums[i];
    cout << getSmallSum(nums, 0, n - 1) << endl;
}
'''
