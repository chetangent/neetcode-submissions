class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-1*stones[i] for i in range(len(stones))]
        heapq.heapify(maxheap)
        while len(maxheap) > 1:
            s1 = heapq.heappop(maxheap)
            s2 = heapq.heappop(maxheap)
            if s1 == s2:
                continue
            else:
                heapq.heappush(maxheap, -1*(s2-s1))
        if not maxheap:
            return 0
        return -1*maxheap[0]
