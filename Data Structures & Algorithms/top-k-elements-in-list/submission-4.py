class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # map = {}
        # for i,n in enumerate(nums):
        #     map[n] = 1 + map.get(n,0)
        # sorted_items = sorted(map.items(), key=lambda x: x[1], reverse=True)
        # result = []
        # for i in range(k):
        #     result.append(sorted_items[i][0])
        # return result
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n,0)
        for n,c in count.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
    
        # count = {}
        # freq = [[] for i in range(len(nums) + 1)]

        # for n in nums:
        #     count[n] = 1 + count.get(n,0)
        # for n,c in count.items():
        #     freq[c].append(n)
        # res = []
        # for i in range(len(freq) - 1, 0, -1):
        #     for n in freq[i]:
        #         res.append(n)
        #         if len(res) == k:
        #             return res

            