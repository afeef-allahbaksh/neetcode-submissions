class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for i,n in enumerate(nums):
            map[n] = 1 + map.get(n,0)
        sorted_items = sorted(map.items(), key=lambda x: x[1], reverse=True)
        result = []
        for i in range(k):
            result.append(sorted_items[i][0])
        return result

            