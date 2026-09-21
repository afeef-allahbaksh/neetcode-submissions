class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, res = 0, 0
        for n in nums:
            if count == 0:
                res = n
            if n == res:
                count += 1
            else:
                count -= 1
        return res
        # count = {}
        # res, maxCount = 0, 0
        # for n in nums:
        #     count[n] = 1 + count.get(n,0)
        #     res = n if count[n] > maxCount else res
        #     maxCount = max(maxCount, count[n])
        # return res