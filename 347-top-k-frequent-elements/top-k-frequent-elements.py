import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        h = {} # val:freq
        for i in nums:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1
        
        # change k:v to -v:k list to heapify
        heap = [(-v,k) for k,v in h.items()]
        heapq.heapify(heap)

        # retrieve top k elements from min-neg heap
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res