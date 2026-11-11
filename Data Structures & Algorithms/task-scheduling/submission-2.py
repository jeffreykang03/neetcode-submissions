class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = defaultdict(int)
        for task in tasks:
            count[task] += 1

        maxf = max(count.values())
        maxCount = 0
        for i in count.values():
            maxCount += 1 if i == maxf else 0

        time = (maxf - 1) * (n + 1) + maxCount
        return max(len(tasks), time)