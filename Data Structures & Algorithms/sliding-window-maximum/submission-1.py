class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import heapq
        maxs = []
        win = []
        ind = 0
        for i in range(k):
            heapq.heappush(win, (-nums[i], i))
        maxs.append(-(win[0][0]))
        ind = k
        # print(win)
        while ind < len(nums):
            heapq.heappush(win, (-nums[ind], ind))
            # print(ind, win[0])
            while win[0][1] < ind-k+1:
                heapq.heappop(win)
            maxs.append(-(win[0][0]))
            ind += 1
        return maxs
