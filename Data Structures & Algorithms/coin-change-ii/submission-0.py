class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp=[[1]+[0]*amount for i in range(len(coins))]
        for i in range(1, amount+1):
            for j in range(len(coins)-1, -1, -1):
                if j<len(coins)-1:
                    dp[j][i]+=dp[j+1][i]
                if i-coins[j]>=0:
                    dp[j][i]+=dp[j][i-coins[j]]
        return dp[0][-1]