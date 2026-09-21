class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * 2 * n

        for i in range(0, 2 * n):
            ans[i] = nums[i % n]

        # Another approach
        # for i in range(0, n):
        #     ans[i] = nums[i]
        #     ans[i] = nums[i * 2]
    
        return ans