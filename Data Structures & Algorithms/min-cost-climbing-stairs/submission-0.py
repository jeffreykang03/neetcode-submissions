class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [float("inf")] * (len(cost) + 3)
        dp[0] = 0
        dp[1] = 0
        for i in range(len(cost)):
            dp[i+1] = min(dp[i+1], dp[i] + cost[i])
            dp[i+2] = min(dp[i+2], dp[i] + cost[i])
        print(dp)
        return min(dp[len(cost)], dp[len(cost) + 1], dp[len(cost) + 2])