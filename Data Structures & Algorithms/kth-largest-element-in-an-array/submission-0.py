class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap = [-1*nums[i] for i in range(len(nums))]
        heapq.heapify(maxheap)
        while k > 0:
            node = heapq.heappop(maxheap)
            k -= 1
        return -1*node