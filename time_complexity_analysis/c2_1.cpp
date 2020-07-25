//
// Created by LiHeng on 2019/8/5.
//
//(1) 大O时间复杂度
//有一个字符串数组，将数组中的每一个字符串按照字母序排序；之后在将整个字符串数组按照字典序排列。计算时间复杂度
//假设最长的字符串长度为s ; 数组中有n个字符串
//两部分： O(n * slogs) + O(s* nlogn)
//第二部分 s* 是因为 2个字符串做比较操作的时间复杂度是O(s)

//(2) 数据规模
//O(n)  10^8次  运行时间大约0.1 - 1.0秒以内
//O(n^2)  10^4次  运行时间大约0.1 - 1.0秒以内
//O(n*logn)  10^7次  运行时间大约1.0秒左右
//保险起见，1秒内能处理的运算次数可以各除10

//(3) 空间复杂度
//递归调用和栈有关，是有空间复杂度消耗的



