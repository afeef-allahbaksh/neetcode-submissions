class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = set(nums)
        return not(len(duplicate) == len(nums))
         