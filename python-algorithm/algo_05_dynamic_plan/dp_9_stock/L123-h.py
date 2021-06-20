# -*- coding: utf-8 -*-

'''
一天结束时，可能有持股、可能未持股、可能卖出过1次、可能卖出过2次、也可能未卖出过

所以定义状态转移数组dp[天数][当前是否持股][卖出的次数]
具体一天结束时的6种状态：

1 未持股，未卖出过股票：说明从未进行过买卖，利润为0
dp[i][0][0]=0

2 未持股，卖出过1次股票：可能是今天卖出，也可能是之前卖的（昨天也未持股且卖出过）
dp[i][0][1]=max(dp[i-1][1][0]+prices[i],dp[i-1][0][1])

3 未持股，卖出过2次股票:可能是今天卖出，也可能是之前卖的（昨天也未持股且卖出过）
dp[i][0][2]=max(dp[i-1][1][1]+prices[i],dp[i-1][0][2])

4 持股，未卖出过股票：可能是今天买的，也可能是之前买的（昨天也持股）
dp[i][1][0]=max(dp[i-1][0][0]-prices[i],dp[i-1][1][0])

5 持股，卖出过1次股票：可能是今天买的，也可能是之前买的（昨天也持股）
dp[i][1][1]=max(dp[i-1][0][1]-prices[i],dp[i-1][1][1])

6 持股，卖出过2次股票：最多交易2次，这种情况不存在
dp[i][1][2]=float('-inf')

'''

# 别人题解
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/solution/zui-jian-dan-2-ge-bian-liang-jie-jue-suo-71fe/
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/solution/5xing-dai-ma-gao-ding-suo-you-gu-piao-ma-j6zo/

