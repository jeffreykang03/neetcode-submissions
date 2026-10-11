class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tot = 0
        ans = 0
        tank = 0
        for i in range(len(gas)):
            tot += gas[i] - cost[i]
            tank += gas[i] - cost[i]
            if tank < 0:
                ans = i + 1
                tank = 0
        if tot < 0:
            return -1
        return ans